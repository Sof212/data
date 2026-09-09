from __future__ import annotations

import gc
from typing import Sequence

import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA

from stats_utils import (
    CACHE_DIR,
    DEVICE,
    GENDER_SETS_FR,
    N_BOOTSTRAP,
    N_PERMUTATIONS,
    OCCUPATIONS,
    RUN_SEAT_TEMPLATES,
    SEED,
    WEAT_CONTRASTS,
    add_fdr,
    model_revision,
    models_of,
    record_model_runtime,
    save_table,
)

DEFINITIONAL_PAIRS = [
    ("homme", "femme"), ("père", "mère"), ("frère", "sœur"),
    ("il", "elle"), ("mari", "épouse"), ("garçon", "fille"),
]


def load_sentence_encoder(model_id: str):
    """Load a sentence encoder pinned to its manifest revision.

    Parameters
    ----------
    model_id : str
        Hub identifier of the encoder.

    Returns
    -------
    sentence_transformers.SentenceTransformer
        Encoder carrying a ``bias_text_prefix`` attribute.

    Notes
    -----
    The E5 model cards recommend the ``query:`` prefix even for symmetric
    tasks, so it is attached to the encoder and applied at encoding time.
    """
    encoder = SentenceTransformer(model_id, device=DEVICE, cache_folder=CACHE_DIR,
                                  revision=model_revision(model_id))
    encoder.bias_text_prefix = "query: " if "multilingual-e5" in model_id else ""
    return encoder


def encode_terms(encoder, terms: Sequence[str], templates: Sequence[str] | None = None) -> np.ndarray:
    """Encode terms, optionally averaged over sentence templates.

    Parameters
    ----------
    encoder : sentence_transformers.SentenceTransformer
        Loaded encoder.
    terms : sequence of str
        Terms to embed.
    templates : sequence of str, optional
        Templates holding a ``{term}`` placeholder. When given, each term is
        embedded inside every template and the vectors are averaged.

    Returns
    -------
    numpy.ndarray
        Array of shape ``(len(terms), dim)`` of normalised embeddings.
    """
    texts = list(terms) if templates is None else [tpl.format(term=t) for t in terms for tpl in templates]
    texts = [getattr(encoder, "bias_text_prefix", "") + x for x in texts]
    emb = encoder.encode(texts, batch_size=32, normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False)
    if templates is None:
        return emb
    return emb.reshape(len(terms), len(templates), -1).mean(axis=1)


def cos(a, b) -> float:
    """Cosine similarity between two vectors.

    Parameters
    ----------
    a, b : array_like
        Vectors of equal dimension.

    Returns
    -------
    float
        Cosine similarity, numerically guarded against a null norm.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


def weat_association(w, A, B) -> float:
    """Differential association of one target with two attribute sets.

    Parameters
    ----------
    w : array_like
        Target embedding.
    A, B : array_like
        Attribute embeddings of the two poles.

    Returns
    -------
    float
        Mean similarity to ``A`` minus mean similarity to ``B``.
    """
    return np.mean([cos(w, a) for a in A]) - np.mean([cos(w, b) for b in B])


def weat_effect_size(X, Y, A, B):
    """Standardised WEAT effect size between two target sets.

    Parameters
    ----------
    X, Y : array_like
        Embeddings of the two target sets, typically male and female names.
    A, B : array_like
        Embeddings of the two attribute poles.

    Returns
    -------
    tuple
        ``(effect_size, s_x, s_y)`` where the two arrays hold the per-item
        associations. The effect size is ``nan`` when the pooled standard
        deviation is null.
    """
    sx = np.array([weat_association(x, A, B) for x in X])
    sy = np.array([weat_association(y, A, B) for y in Y])
    pooled = np.concatenate([sx, sy]).std(ddof=1)
    effect = (sx.mean() - sy.mean()) / pooled if np.isfinite(pooled) and pooled > 0 else np.nan
    return float(effect), sx, sy


def weat_permutation_p(X, Y, A, B, n=None, seed: int = SEED) -> float:
    """Permutation p-value of a WEAT effect size.

    Parameters
    ----------
    X, Y : array_like
        Embeddings of the two target sets.
    A, B : array_like
        Embeddings of the two attribute poles.
    n : int, optional
        Number of permutations; defaults to ``N_PERMUTATIONS``.
    seed : int, optional
        Seed of the permutation generator.

    Returns
    -------
    float
        Two-sided p-value, or ``nan`` when the pooled standard deviation is
        null.

    Notes
    -----
    Associations are computed once and only the X/Y assignment is permuted,
    which keeps the test tractable at ten thousand permutations.
    """
    n = int(n or N_PERMUTATIONS)
    combined = np.vstack([X, Y])
    nx = len(X)
    scores = np.array([weat_association(item, A, B) for item in combined])
    pooled = scores.std(ddof=1)
    if not np.isfinite(pooled) or pooled <= 0:
        return np.nan
    observed = abs((scores[:nx].mean() - scores[nx:].mean()) / pooled)
    rng = np.random.default_rng(seed)
    exceedances = 0
    for _ in range(n):
        idx = rng.permutation(len(scores))
        effect = abs((scores[idx[:nx]].mean() - scores[idx[nx:]].mean()) / pooled)
        exceedances += int(effect >= observed)
    return float((exceedances + 1) / (n + 1))


def weat_bootstrap_ci(X, Y, A, B, n=None, seed: int = SEED) -> tuple[float, float]:
    """Bootstrap confidence interval of a WEAT effect size.

    Parameters
    ----------
    X, Y : array_like
        Embeddings of the two target sets.
    A, B : array_like
        Embeddings of the two attribute poles.
    n : int, optional
        Number of resamples; defaults to ``N_BOOTSTRAP``.
    seed : int, optional
        Seed of the resampling generator.

    Returns
    -------
    tuple of float
        Lower and upper bounds at the 95 % level; all four sets are resampled
        jointly.
    """
    rng = np.random.default_rng(seed)
    n = n or N_BOOTSTRAP
    values = []
    for _ in range(n):
        xr = X[rng.integers(0, len(X), len(X))]
        yr = Y[rng.integers(0, len(Y), len(Y))]
        ar = A[rng.integers(0, len(A), len(A))]
        br = B[rng.integers(0, len(B), len(B))]
        values.append(weat_effect_size(xr, yr, ar, br)[0])
    return float(np.quantile(values, .025)), float(np.quantile(values, .975))


def run_weat(encoder, model_id: str, contextual: bool = False) -> pd.DataFrame:
    """Score the six gender contrasts on one encoder.

    Parameters
    ----------
    encoder : sentence_transformers.SentenceTransformer
        Loaded encoder.
    model_id : str
        Hub identifier, copied into the output.
    contextual : bool, optional
        ``False`` embeds bare terms (WEAT), ``True`` embeds them inside the
        eighteen retained templates (SEAT).

    Returns
    -------
    pandas.DataFrame
        One row per contrast with the effect size, its permutation p-value,
        the bootstrap bounds and the set sizes.
    """
    templates = RUN_SEAT_TEMPLATES if contextual else None
    E = {k: encode_terms(encoder, v, templates) for k, v in GENDER_SETS_FR.items()}
    rows = []
    for test, a, b in WEAT_CONTRASTS:
        effect, sx, sy = weat_effect_size(E["male_names"], E["female_names"], E[a], E[b])
        ci_low, ci_high = weat_bootstrap_ci(E["male_names"], E["female_names"], E[a], E[b])
        rows.append(dict(model_id=model_id, metric="SEAT" if contextual else "WEAT", test=test,
                         effect_size=effect,
                         p_value=weat_permutation_p(E["male_names"], E["female_names"], E[a], E[b]),
                         ci_low=ci_low, ci_high=ci_high, n_x=len(sx), n_y=len(sy)))
    return pd.DataFrame(rows)


def gender_direction_pca(encoder, pairs: Sequence[tuple[str, str]], templates=None):
    """Estimate a gender direction from definitional pairs.

    Parameters
    ----------
    encoder : sentence_transformers.SentenceTransformer
        Loaded encoder.
    pairs : sequence of tuple of str
        Definitional pairs such as ``("homme", "femme")``.
    templates : sequence of str, optional
        Templates used to contextualise each term.

    Returns
    -------
    tuple
        ``(direction, explained_variance_ratio)``; the direction is the first
        principal component of the symmetrised difference vectors.
    """
    diffs = []
    for male, female in pairs:
        em = encode_terms(encoder, [male], templates)[0]
        ef = encode_terms(encoder, [female], templates)[0]
        diffs.extend([em - ef, ef - em])
    pca = PCA(n_components=min(3, len(diffs), len(diffs[0])))
    pca.fit(np.vstack(diffs))
    return pca.components_[0], pca.explained_variance_ratio_


def run_direct_bias(encoder, model_id: str) -> pd.DataFrame:
    """Project every occupation onto the gender direction.

    Parameters
    ----------
    encoder : sentence_transformers.SentenceTransformer
        Loaded encoder.
    model_id : str
        Hub identifier, copied into the output.

    Returns
    -------
    pandas.DataFrame
        Signed and absolute projection of each occupation, plus the variance
        explained by the gender component.

    Notes
    -----
    The sign depends on the orientation of the estimated direction and
    carries no meaning on its own.
    """
    direction, variance = gender_direction_pca(encoder, DEFINITIONAL_PAIRS, templates=RUN_SEAT_TEMPLATES)
    occ = encode_terms(encoder, OCCUPATIONS, RUN_SEAT_TEMPLATES)
    projections = occ @ direction
    return pd.DataFrame({"model_id": model_id, "occupation": OCCUPATIONS,
                         "gender_projection": projections, "abs_projection": np.abs(projections),
                         "gender_pc_variance": variance[0]})


def contextual_effect_distribution(encoder) -> pd.DataFrame:
    """Recompute the career/family effect size template by template.

    Parameters
    ----------
    encoder : sentence_transformers.SentenceTransformer
        Loaded encoder.

    Returns
    -------
    pandas.DataFrame
        One row per template with its effect size, showing how sensitive
        SEAT is to the carrier sentence.
    """
    effects = []
    for template in RUN_SEAT_TEMPLATES:
        E = {k: encode_terms(encoder, GENDER_SETS_FR[k], [template])
             for k in ("male_names", "female_names", "career", "family")}
        d, _, _ = weat_effect_size(E["male_names"], E["female_names"], E["career"], E["family"])
        effects.append({"template": template, "effect_size": d})
    return pd.DataFrame(effects)


def run_embedding_family(save: bool = True):
    """Run the whole embedding family on the three active encoders.

    Parameters
    ----------
    save : bool, optional
        Write the three result tables to disk.

    Returns
    -------
    tuple of pandas.DataFrame
        ``(embed_df, direct_df, context_df)``: WEAT and SEAT results with FDR
        correction, direct-bias projections, and per-template sensitivity.

    Notes
    -----
    Downloads several hundred megabytes of weights on a fresh machine. Each
    encoder is released before the next one is loaded.
    """
    embedding_results, direct_results, context_results = [], [], []
    for model_id in models_of("sentence_embedding"):
        print("Embedding:", model_id)
        encoder = load_sentence_encoder(model_id)
        record_model_runtime(model_id, encoder, "embedding")
        embedding_results += [run_weat(encoder, model_id, False), run_weat(encoder, model_id, True)]
        direct_results.append(run_direct_bias(encoder, model_id))
        context_results.append(contextual_effect_distribution(encoder).assign(model_id=model_id))
        del encoder
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    embed_df = add_fdr(pd.concat(embedding_results, ignore_index=True)) if embedding_results else pd.DataFrame()
    direct_df = pd.concat(direct_results, ignore_index=True) if direct_results else pd.DataFrame()
    context_df = pd.concat(context_results, ignore_index=True) if context_results else pd.DataFrame()

    if save:
        if not embed_df.empty:
            save_table(embed_df, "embedding_weat_seat")
        if not direct_df.empty:
            save_table(direct_df, "embedding_direct_bias")
        if not context_df.empty:
            save_table(context_df, "embedding_context_sensitivity")
    return embed_df, direct_df, context_df
