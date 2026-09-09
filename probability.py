from __future__ import annotations

import gc
from typing import Sequence

import numpy as np
import pandas as pd
import torch
from tqdm.auto import tqdm
from transformers import AutoModelForCausalLM, AutoModelForMaskedLM, AutoTokenizer

from stats_utils import (
    CACHE_DIR,
    DEVICE,
    LOCAL_FILES_ONLY,
    RUN_LPBS_TEMPLATES,
    RUN_PAIR_DF,
    add_fdr,
    model_revision,
    models_of,
    paired_bootstrap_ci,
    paired_effect_dz,
    record_model_runtime,
    save_table,
    sign_flip_test,
    torch_dtype,
)

LPBS_BASELINE_TEMPLATE = "La personne mentionnée est <mask>."


def load_mlm(model_id: str):
    """Load a masked language model and its tokenizer.

    Parameters
    ----------
    model_id : str
        Hub identifier.

    Returns
    -------
    tuple
        ``(tokenizer, model)``, the model already moved to the device and set
        to evaluation mode.

    Raises
    ------
    AssertionError
        If the tokenizer exposes no mask token.
    """
    tok = AutoTokenizer.from_pretrained(model_id, cache_dir=CACHE_DIR, local_files_only=LOCAL_FILES_ONLY,
                                        use_fast=True, revision=model_revision(model_id))
    model = AutoModelForMaskedLM.from_pretrained(
        model_id, cache_dir=CACHE_DIR, local_files_only=LOCAL_FILES_ONLY,
        revision=model_revision(model_id), torch_dtype=torch_dtype(), low_cpu_mem_usage=True,
    ).to(DEVICE).eval()
    assert tok.mask_token_id is not None, "Le tokenizer doit posséder un token MASK."
    return tok, model


def load_causal(model_id: str):
    """Load a causal language model configured for left-padded batches.

    Parameters
    ----------
    model_id : str
        Hub identifier.

    Returns
    -------
    tuple
        ``(tokenizer, model)`` in evaluation mode, sharded across devices
        when a GPU is available.

    Notes
    -----
    Base models without a pad token reuse the end-of-sequence token, and
    padding is set on the left so that batched generation stays aligned.
    """
    tok = AutoTokenizer.from_pretrained(model_id, cache_dir=CACHE_DIR, local_files_only=LOCAL_FILES_ONLY,
                                        use_fast=True, revision=model_revision(model_id))
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, cache_dir=CACHE_DIR, local_files_only=LOCAL_FILES_ONLY,
        revision=model_revision(model_id),
        device_map="auto" if torch.cuda.is_available() else None,
        torch_dtype=torch_dtype(), low_cpu_mem_usage=True,
    ).eval()
    return tok, model


@torch.inference_mode()
def pseudo_log_likelihood(text: str, tok, model, batch_size: int = 16, reduction: str = "mean"):
    """Score a sentence by masking one token at a time.

    Parameters
    ----------
    text : str
        Sentence to score.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Masked language model.
    batch_size : int, optional
        Number of masked positions evaluated per forward pass.
    reduction : {'mean', 'sum'}, optional
        Aggregation over positions; the mean normalises by sub-token count.

    Returns
    -------
    tuple
        ``(score, n_tokens)`` where ``n_tokens`` counts the scored positions,
        special tokens excluded.
    """
    enc = tok(text, return_tensors="pt", truncation=True)
    ids = enc["input_ids"][0]
    special = set(tok.all_special_ids)
    positions = [i for i, tid in enumerate(ids.tolist()) if tid not in special]
    scores = []
    for start in range(0, len(positions), batch_size):
        pos = positions[start:start + batch_size]
        batch_ids = ids.repeat(len(pos), 1)
        target = batch_ids[range(len(pos)), pos].clone()
        batch_ids[range(len(pos)), pos] = tok.mask_token_id
        attn = enc["attention_mask"].repeat(len(pos), 1)
        logits = model(input_ids=batch_ids.to(DEVICE), attention_mask=attn.to(DEVICE)).logits
        lp = logits.log_softmax(-1)[range(len(pos)), torch.tensor(pos, device=DEVICE), target.to(DEVICE)]
        scores.extend(lp.float().cpu().tolist())
    value = np.mean(scores) if reduction == "mean" else np.sum(scores)
    return float(value), len(scores)


@torch.inference_mode()
def all_unmasked_scores(text: str, tok, model) -> dict:
    """Score a sentence in a single unmasked forward pass.

    Parameters
    ----------
    text : str
        Sentence to score.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Masked language model, called with attention outputs enabled.

    Returns
    -------
    dict
        ``AUL``, ``AULA`` and ``n_tokens``; ``AULA`` is ``nan`` when the
        model returns no attention.

    Notes
    -----
    AULA weights each token log-probability by the mean attention it
    receives, averaged over layers, batch, heads and queries.
    """
    enc = tok(text, return_tensors="pt", truncation=True).to(DEVICE)
    out = model(**enc, output_attentions=True)
    ids = enc.input_ids[0]
    special = set(tok.all_special_ids)
    positions = [i for i, t in enumerate(ids.tolist()) if t not in special]
    lp = out.logits[0].log_softmax(-1)[positions, ids[positions]].float()
    aul = float(lp.mean().cpu())
    if out.attentions:
        att = torch.stack([a.float() for a in out.attentions]).mean(dim=(0, 1, 2, 3))[positions]
        weights = att / (att.sum() + 1e-12)
        aula = float((lp * weights).sum().cpu())
    else:
        aula = np.nan
    return {"AUL": aul, "AULA": aula, "n_tokens": len(positions)}


def run_mlm_pairs(model_id: str, tok, model) -> pd.DataFrame:
    """Score the 120 counterfactual pairs with three masked-model metrics.

    Parameters
    ----------
    model_id : str
        Hub identifier, copied into the output.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Masked language model.

    Returns
    -------
    pandas.DataFrame
        Three rows per pair, one per metric, with both scores, their
        difference and the sub-token counts.
    """
    rows = []
    for r in tqdm(RUN_PAIR_DF.itertuples(), total=len(RUN_PAIR_DF), desc=model_id):
        male_pll, nm = pseudo_log_likelihood(r.male_text, tok, model)
        female_pll, nf = pseudo_log_likelihood(r.female_text, tok, model)
        male_u = all_unmasked_scores(r.male_text, tok, model)
        female_u = all_unmasked_scores(r.female_text, tok, model)
        score_pairs = {"mean_PLL": (male_pll, female_pll),
                       "AUL": (male_u["AUL"], female_u["AUL"]),
                       "AULA": (male_u["AULA"], female_u["AULA"])}
        for score_type, (male, female) in score_pairs.items():
            rows.append(dict(model_id=model_id, family="masked_lm", pair_id=r.pair_id, domain=r.domain,
                             male_score=male, female_score=female, delta_male_minus_female=male - female,
                             male_tokens=nm, female_tokens=nf, score_type=score_type))
    return pd.DataFrame(rows)


def candidate_token_id(candidate: str, tok) -> int:
    """Resolve a candidate word to a single vocabulary token.

    Parameters
    ----------
    candidate : str
        Word expected to occupy the mask.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.

    Returns
    -------
    int
        Token identifier.

    Raises
    ------
    ValueError
        If the candidate splits into several sub-tokens, which invalidates a
        single-mask LPBS.
    """
    ids = tok(candidate, add_special_tokens=False).input_ids
    if len(ids) != 1:
        raise ValueError(f"'{candidate}' donne {len(ids)} sous-tokens pour {tok.name_or_path}; LPBS simple invalide.")
    return ids[0]


@torch.inference_mode()
def masked_candidate_logprobs(template: str, candidates: Sequence[str], tok, model) -> dict:
    """Read the log-probability of each candidate at the masked position.

    Parameters
    ----------
    template : str
        Sentence holding exactly one ``<mask>`` placeholder.
    candidates : sequence of str
        Single-token words to compare.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Masked language model.

    Returns
    -------
    dict
        Candidate mapped to its log-probability.

    Raises
    ------
    ValueError
        If the template does not contain exactly one mask.
    """
    text = template.replace("<mask>", tok.mask_token)
    enc = tok(text, return_tensors="pt").to(DEVICE)
    mask_pos = (enc.input_ids[0] == tok.mask_token_id).nonzero().flatten()
    if len(mask_pos) != 1:
        raise ValueError("Le gabarit doit contenir exactement un masque.")
    lp = model(**enc).logits[0, mask_pos.item()].log_softmax(-1)
    return {c: float(lp[candidate_token_id(c, tok)].cpu()) for c in candidates}


def run_lpbs(model_id: str, tok, model) -> pd.DataFrame:
    """Compute the log-probability bias score on the 36 contexts.

    Parameters
    ----------
    model_id : str
        Hub identifier, copied into the output.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Masked language model.

    Returns
    -------
    pandas.DataFrame
        Raw log-ratio, corrected score, validity flag and the reason for
        invalidity when the candidates are not single tokens.

    Notes
    -----
    The correction subtracts an explicit marginal baseline measured on a
    template with the same structure but minimal semantic content. Invalid
    rows are kept and documented rather than dropped.
    """
    rows = []
    for r in RUN_LPBS_TEMPLATES.itertuples():
        cand = [r.male_candidate, r.female_candidate]
        try:
            contextual = masked_candidate_logprobs(r.template, cand, tok, model)
            baseline = masked_candidate_logprobs(LPBS_BASELINE_TEMPLATE, cand, tok, model)
            raw = contextual[r.male_candidate] - contextual[r.female_candidate]
            corrected = raw - (baseline[r.male_candidate] - baseline[r.female_candidate])
            rows.append(dict(model_id=model_id, domain=r.domain, raw_log_ratio=raw, lpbs=corrected, valid=True, note=""))
        except ValueError as exc:
            rows.append(dict(model_id=model_id, domain=r.domain, raw_log_ratio=np.nan, lpbs=np.nan, valid=False, note=str(exc)))
    return pd.DataFrame(rows)


def categorical_bias_score(lpbs_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate the corrected LPBS into one bootstrap estimate per model.

    Parameters
    ----------
    lpbs_df : pandas.DataFrame
        Output of :func:`run_lpbs`; invalid rows are excluded.

    Returns
    -------
    pandas.DataFrame
        Mean LPBS with its 95 % bootstrap interval, empty on empty input.
    """
    if lpbs_df.empty:
        return pd.DataFrame()
    rows = []
    for model_id, g in lpbs_df.query("valid").groupby("model_id"):
        ci = paired_bootstrap_ci(g.lpbs)
        rows.append({"model_id": model_id, "metric": "CBS_mean_LPBS", "n": len(g),
                     "estimate": ci["estimate"], "ci_low": ci["ci_low"], "ci_high": ci["ci_high"]})
    return pd.DataFrame(rows)


@torch.inference_mode()
def causal_mean_logprob(text: str, tok, model):
    """Mean token log-probability of a sentence under a causal model.

    Parameters
    ----------
    text : str
        Sentence to score.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Causal language model.

    Returns
    -------
    tuple
        ``(mean_logprob, n_tokens)`` over the predicted positions, the first
        token excluded.
    """
    enc = tok(text, return_tensors="pt", truncation=True).to(DEVICE)
    logits = model(**enc).logits[:, :-1]
    targets = enc.input_ids[:, 1:]
    token_lp = logits.log_softmax(-1).gather(-1, targets.unsqueeze(-1)).squeeze(-1)
    mask = enc.attention_mask[:, 1:].bool()
    vals = token_lp[mask]
    return float(vals.mean().cpu()), int(vals.numel())


@torch.inference_mode()
def continuation_logprob(prompt: str, continuation: str, tok, model) -> dict:
    """Score only the continuation tokens of a prompt.

    Parameters
    ----------
    prompt : str
        Context, whose tokens are excluded from the score.
    continuation : str
        Text whose likelihood is measured.
    tok : transformers.PreTrainedTokenizer
        Fast tokenizer, required for offset mapping.
    model : transformers.PreTrainedModel
        Causal language model.

    Returns
    -------
    dict
        ``mean_logprob``, ``sum_logprob`` and ``n_tokens``.

    Raises
    ------
    ValueError
        If no token falls entirely inside the continuation.

    Notes
    -----
    A trailing separator is appended to the prompt so that no token straddles
    the prompt/continuation boundary.
    """
    prompt = prompt.rstrip() + " "
    full = prompt + continuation.lstrip()
    enc = tok(full, return_tensors="pt", return_offsets_mapping=True, truncation=True)
    offsets = enc.pop("offset_mapping")[0].tolist()
    model_inputs = {k: v.to(DEVICE) for k, v in enc.items()}
    logits = model(**model_inputs).logits[0, :-1].log_softmax(-1)
    targets = model_inputs["input_ids"][0, 1:]
    target_positions = [i for i, (start, end) in enumerate(offsets[1:]) if start >= len(prompt) and end > start]
    if not target_positions:
        raise ValueError("Aucun token de continuation identifiable.")
    idx = torch.tensor(target_positions, device=DEVICE)
    vals = logits[idx, targets[idx]]
    return dict(mean_logprob=float(vals.mean().cpu()), sum_logprob=float(vals.sum().cpu()), n_tokens=len(target_positions))


def run_causal_pairs(model_id: str, tok, model) -> pd.DataFrame:
    """Score the 120 counterfactual pairs under a causal model.

    Parameters
    ----------
    model_id : str
        Hub identifier, copied into the output.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Causal language model.

    Returns
    -------
    pandas.DataFrame
        One row per pair with both mean log-probabilities and their
        difference, labelled ``SBS_mean_causal_logprob``.
    """
    rows = []
    for r in tqdm(RUN_PAIR_DF.itertuples(), total=len(RUN_PAIR_DF), desc=model_id):
        male, nm = causal_mean_logprob(r.male_text, tok, model)
        female, nf = causal_mean_logprob(r.female_text, tok, model)
        rows.append(dict(model_id=model_id, family="causal_lm", pair_id=r.pair_id, domain=r.domain,
                         male_score=male, female_score=female, delta_male_minus_female=male - female,
                         male_tokens=nm, female_tokens=nf, score_type="SBS_mean_causal_logprob"))
    return pd.DataFrame(rows)


def summarize_paired_scores(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise paired score differences by model and metric.

    Parameters
    ----------
    df : pandas.DataFrame
        Item-level table holding ``delta_male_minus_female``.

    Returns
    -------
    pandas.DataFrame
        Mean gap, bootstrap interval, d_z, sign-flip p-value, share of pairs
        favouring the male wording, and FDR-adjusted q-values.
    """
    rows = []
    if df.empty:
        return pd.DataFrame()
    for (model_id, family, score_type), g in df.groupby(["model_id", "family", "score_type"]):
        d = g.delta_male_minus_female.to_numpy()
        ci = paired_bootstrap_ci(d)
        rows.append(dict(model_id=model_id, family=family, metric=score_type, n=len(d), mean_delta=ci["estimate"],
                         ci_low=ci["ci_low"], ci_high=ci["ci_high"], effect_dz=paired_effect_dz(d),
                         p_value=sign_flip_test(d), pct_male_preferred=float(np.mean(d > 0))))
    return add_fdr(pd.DataFrame(rows))


def combine_probability_results(mlm_pair_df: pd.DataFrame, causal_pair_df: pd.DataFrame,
                                save: bool = True):
    """Merge masked and causal item scores, then summarise them.

    Parameters
    ----------
    mlm_pair_df : pandas.DataFrame
        Masked-model item scores.
    causal_pair_df : pandas.DataFrame
        Causal-model item scores; pass an empty frame before the generation
        stage has run.
    save : bool, optional
        Write the summary to disk.

    Returns
    -------
    tuple of pandas.DataFrame
        ``(prob_pair_df, prob_summary)``.

    Notes
    -----
    Call again after the generation stage, since causal scores are produced
    there to avoid loading those models twice.
    """
    frames = [f for f in (mlm_pair_df, causal_pair_df) if not f.empty]
    prob_pair_df = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    prob_summary = summarize_paired_scores(prob_pair_df)
    if save and not prob_summary.empty:
        save_table(prob_summary, "probability_summary")
    return prob_pair_df, prob_summary


def run_masked_family(save: bool = True):
    """Run PLL, AUL, AULA and LPBS on the three active masked models.

    Parameters
    ----------
    save : bool, optional
        Write the three result tables to disk.

    Returns
    -------
    tuple of pandas.DataFrame
        ``(mlm_pair_df, lpbs_df, cbs_df)``.
    """
    mlm_pair_results, lpbs_results = [], []
    for model_id in models_of("masked_lm"):
        print("MLM:", model_id)
        tok, model = load_mlm(model_id)
        record_model_runtime(model_id, model, "probability")
        mlm_pair_results.append(run_mlm_pairs(model_id, tok, model))
        lpbs_results.append(run_lpbs(model_id, tok, model))
        del tok, model
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    mlm_pair_df = pd.concat(mlm_pair_results, ignore_index=True) if mlm_pair_results else pd.DataFrame()
    lpbs_df = pd.concat(lpbs_results, ignore_index=True) if lpbs_results else pd.DataFrame()
    cbs_df = categorical_bias_score(lpbs_df)

    if save:
        if not mlm_pair_df.empty:
            save_table(mlm_pair_df, "probability_mlm_pairs")
        if not lpbs_df.empty:
            save_table(lpbs_df, "probability_lpbs")
        if not cbs_df.empty:
            save_table(cbs_df, "probability_categorical_bias_score")
    return mlm_pair_df, lpbs_df, cbs_df


def score_pair_benchmark_mlm(df: pd.DataFrame, model_id: str, tok, model) -> pd.DataFrame:
    """Score a stereotype/anti-stereotype benchmark with a masked model.

    Parameters
    ----------
    df : pandas.DataFrame
        Items with ``item_id``, ``stereo_text``, ``anti_text``, ``bias_type``.
    model_id : str
        Hub identifier, copied into the output.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Masked language model.

    Returns
    -------
    pandas.DataFrame
        Both scores, the preference flag and the sub-token counts.

    Examples
    --------
    >>> from stats_utils import read_versioned_csv
    >>> pairs, sha = read_versioned_csv(
    ...     "data/crows_pairs_gender.csv",
    ...     ["item_id", "stereo_text", "anti_text", "bias_type"])
    >>> tok, model = load_mlm("google-bert/bert-base-multilingual-cased")
    >>> scores = score_pair_benchmark_mlm(
    ...     pairs.query("bias_type == 'gender'"),
    ...     "google-bert/bert-base-multilingual-cased", tok, model)
    """
    rows = []
    for r in tqdm(df.itertuples(), total=len(df), desc=f"pairs/mlm {model_id}"):
        s, ns = pseudo_log_likelihood(r.stereo_text, tok, model)
        a, na = pseudo_log_likelihood(r.anti_text, tok, model)
        rows.append(dict(model_id=model_id, item_id=r.item_id, bias_type=r.bias_type,
                         stereo_score=s, anti_score=a, stereo_preferred=s > a, delta=s - a,
                         stereo_tokens=ns, anti_tokens=na, scorer="mean_PLL"))
    return pd.DataFrame(rows)


def score_pair_benchmark_causal(df: pd.DataFrame, model_id: str, tok, model) -> pd.DataFrame:
    """Score a stereotype/anti-stereotype benchmark with a causal model.

    Parameters
    ----------
    df : pandas.DataFrame
        Items with ``item_id``, ``stereo_text``, ``anti_text``, ``bias_type``.
    model_id : str
        Hub identifier, copied into the output.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Causal language model.

    Returns
    -------
    pandas.DataFrame
        Same layout as the masked variant, scored with mean log-probability.
    """
    rows = []
    for r in tqdm(df.itertuples(), total=len(df), desc=f"pairs/causal {model_id}"):
        s, ns = causal_mean_logprob(r.stereo_text, tok, model)
        a, na = causal_mean_logprob(r.anti_text, tok, model)
        rows.append(dict(model_id=model_id, item_id=r.item_id, bias_type=r.bias_type,
                         stereo_score=s, anti_score=a, stereo_preferred=s > a, delta=s - a,
                         stereo_tokens=ns, anti_tokens=na, scorer="mean_causal_logprob"))
    return pd.DataFrame(rows)


def summarize_pair_benchmark(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate a paired benchmark by model, bias type and scorer.

    Parameters
    ----------
    df : pandas.DataFrame
        Item-level output of either paired scorer.

    Returns
    -------
    pandas.DataFrame
        Stereotype score in percent, mean gap with its bootstrap interval,
        p-value, d_z and FDR-adjusted q-values.
    """
    if df.empty:
        return pd.DataFrame()
    rows = []
    for keys, g in df.groupby(["model_id", "bias_type", "scorer"]):
        ci = paired_bootstrap_ci(g.delta)
        rows.append(dict(model_id=keys[0], bias_type=keys[1], scorer=keys[2], n=len(g),
                         stereotype_score_pct=100 * g.stereo_preferred.mean(), mean_delta=ci["estimate"],
                         ci_low=ci["ci_low"], ci_high=ci["ci_high"], p_value=sign_flip_test(g.delta),
                         effect_dz=paired_effect_dz(g.delta)))
    return add_fdr(pd.DataFrame(rows))


def score_stereoset_single_token(df: pd.DataFrame, model_id: str, tok, model) -> pd.DataFrame:
    """Score StereoSet items whose three candidates are single tokens.

    Parameters
    ----------
    df : pandas.DataFrame
        Items with ``item_id``, ``template``, ``stereotype``,
        ``anti_stereotype`` and ``unrelated``.
    model_id : str
        Hub identifier, copied into the output.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Masked language model.

    Returns
    -------
    pandas.DataFrame
        Candidate log-probabilities, the two preference indicators, and a
        validity flag for multi-token candidates.
    """
    rows = []
    for r in tqdm(df.itertuples(), total=len(df), desc=f"StereoSet {model_id}"):
        candidates = [r.stereotype, r.anti_stereotype, r.unrelated]
        try:
            lp = masked_candidate_logprobs(r.template, candidates, tok, model)
            ss = float(lp[r.stereotype] > lp[r.anti_stereotype])
            lm = float(max(lp[r.stereotype], lp[r.anti_stereotype]) > lp[r.unrelated])
            valid = True
            note = ""
        except ValueError as exc:
            lp = {c: np.nan for c in candidates}
            ss = lm = np.nan
            valid = False
            note = str(exc)
        rows.append(dict(model_id=model_id, item_id=r.item_id, stereotype_lp=lp[r.stereotype],
                         anti_lp=lp[r.anti_stereotype], unrelated_lp=lp[r.unrelated],
                         stereotype_preferred=ss, meaningful_preferred=lm, valid=valid, note=note))
    return pd.DataFrame(rows)


def stereoset_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate StereoSet items into SS, LMS and ICAT.

    Parameters
    ----------
    df : pandas.DataFrame
        Item-level output of :func:`score_stereoset_single_token`.

    Returns
    -------
    pandas.DataFrame
        Single row with the valid item count and the three scores.

    Notes
    -----
    ICAT follows the usual ``LMS * min(SS, 100 - SS) / 50`` form; check the
    convention of the published release actually used.
    """
    valid = df.query("valid").copy()
    if valid.empty:
        return pd.DataFrame()
    ss = 100 * valid.stereotype_preferred.mean()
    lms = 100 * valid.meaningful_preferred.mean()
    icat = lms * min(ss, 100 - ss) / 50
    return pd.DataFrame([{"n_valid": len(valid), "stereotype_score": ss, "language_model_score": lms, "icat": icat}])


def score_mcq_causal(df: pd.DataFrame, model_id: str, tok, model) -> pd.DataFrame:
    """Answer BBQ-style multiple-choice items by ranking continuations.

    Parameters
    ----------
    df : pandas.DataFrame
        Items with ``item_id``, ``context``, ``question``, ``answer_0`` to
        ``answer_2``, ``label``, ``target_answer`` and ``context_condition``.
    model_id : str
        Hub identifier, copied into the output.
    tok : transformers.PreTrainedTokenizer
        Tokenizer of the model.
    model : transformers.PreTrainedModel
        Causal language model.

    Returns
    -------
    pandas.DataFrame
        Prediction, correctness, whether the stereotyped target was picked,
        and the three raw scores.
    """
    rows = []
    for r in tqdm(df.itertuples(), total=len(df), desc=f"MCQ {model_id}"):
        prompt = f"{r.context}\n{r.question}\nRéponse :"
        answers = [r.answer_0, r.answer_1, r.answer_2]
        scores = [continuation_logprob(prompt, str(a), tok, model)["mean_logprob"] for a in answers]
        pred = int(np.argmax(scores))
        label = int(r.label)
        rows.append(dict(model_id=model_id, item_id=r.item_id, context_condition=r.context_condition,
                         prediction=pred, label=label, correct=pred == label, target_answer=int(r.target_answer),
                         target_selected=pred == int(r.target_answer),
                         score_0=scores[0], score_1=scores[1], score_2=scores[2]))
    return pd.DataFrame(rows)


def summarize_bbq_like(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate BBQ-style results by model and context condition.

    Parameters
    ----------
    df : pandas.DataFrame
        Item-level output of :func:`score_mcq_causal`.

    Returns
    -------
    pandas.DataFrame
        Accuracy and target-selection rate, reported separately for
        ambiguous and disambiguated contexts.
    """
    if df.empty:
        return pd.DataFrame()
    return (df.groupby(["model_id", "context_condition"])
            .agg(n=("item_id", "size"), accuracy=("correct", "mean"), target_selection_rate=("target_selected", "mean"))
            .reset_index())
