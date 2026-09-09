from __future__ import annotations

import json
import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

from stats_utils import (
    FIGURE_DPI,
    FIGURE_FORMATS,
    FIG_DIR,
    GENDER_SETS_FR,
    GENERATION_PAIRS,
    MODEL_REGISTRY,
    PAIR_DF,
    SEED,
    format_params_m,
    model_meta,
    model_order,
    require_columns,
    symmetric_limit,
)

SIZE_COLORS = {"small": "#0072B2", "medium": "#E69F00", "large": "#009E73"}
GROUP_COLORS = {"male": "#0072B2", "female": "#CC79A7"}
FAMILY_COLORS = {"embedding": "#56B4E9", "probability": "#E69F00", "generation": "#009E73"}
SIZE_MARKERS = {"small": "o", "medium": "s", "large": "D"}

FIGURE_CATALOG: list[dict] = []


def apply_theme() -> None:
    """Install the editorial chart theme.

    Notes
    -----
    Colour-blind safe palette, print-legible sizes and embedded fonts, so
    every figure of the dissertation stays visually consistent. Call once
    before producing figures.
    """
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.25)
    mpl.rcParams.update({
        "figure.dpi": 140, "savefig.dpi": 600, "figure.facecolor": "white", "axes.facecolor": "white",
        "font.family": "DejaVu Sans", "font.size": 10.5, "axes.titlesize": 12.5, "axes.titleweight": "bold",
        "axes.labelsize": 10.5, "xtick.labelsize": 9.5, "ytick.labelsize": 9.5, "legend.fontsize": 9,
        "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": .8,
        "grid.color": "#D9D9D9", "grid.linewidth": .6, "grid.alpha": .7,
        "lines.linewidth": 1.8, "lines.markersize": 6, "errorbar.capsize": 3,
        "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none",
    })


def panel_label(ax, label: str) -> None:
    """Place a bold panel letter above the top-left corner of an axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axis.
    label : str
        Panel letter, such as ``"A"``.
    """
    ax.text(-.08, 1.04, label, transform=ax.transAxes, fontsize=12, fontweight="bold", va="bottom")


def finish_axis(ax, zero: bool = False, percent: bool = False) -> None:
    """Apply the shared grid and axis conventions.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axis.
    zero : bool, optional
        Draw a reference line at zero.
    percent : bool, optional
        Format the horizontal axis as percentages.
    """
    if zero:
        ax.axvline(0, color="#333333", lw=.9, zorder=0)
    if percent:
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f} %"))
    ax.grid(axis="x", visible=True)
    ax.grid(axis="y", visible=False)


def save_figure(fig, stem: str, caption: str = "", source: str = "Calculs de l'auteur") -> None:
    """Export a figure in every configured format and log its caption.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to export.
    stem : str
        File name without extension.
    caption : str, optional
        Caption stored in the JSON catalogue.
    source : str, optional
        Source line stored alongside the caption.
    """
    fig.align_labels()
    for fmt in FIGURE_FORMATS:
        kwargs = {"dpi": FIGURE_DPI} if fmt == "png" else {}
        fig.savefig(FIG_DIR / f"{stem}.{fmt}", bbox_inches="tight", facecolor="white", **kwargs)
    FIGURE_CATALOG.append({
        "stem": stem, "caption": caption, "source": source,
        "formats": list(FIGURE_FORMATS), "dpi_png": FIGURE_DPI,
    })
    (FIG_DIR / "figure_catalog.json").write_text(
        json.dumps(FIGURE_CATALOG, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def close_figure(fig, stem: str, caption: str, show: bool) -> None:
    """Export, optionally display, then release a figure.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to finalise.
    stem : str
        File name without extension.
    caption : str
        Caption stored in the catalogue.
    show : bool
        Display the figure before closing it.
    """
    save_figure(fig, stem, caption)
    if show:
        plt.show()
    plt.close(fig)


def plot_design_3x3(show: bool = True) -> None:
    """Draw the nine model sizes, one panel per benchmark family.

    Parameters
    ----------
    show : bool, optional
        Display the figure in addition to saving it.
    """
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.4), sharex=True, constrained_layout=True)
    families = list(MODEL_REGISTRY.benchmark_family.unique())
    for ax, (family, g) in zip(axes, MODEL_REGISTRY.groupby("benchmark_family", sort=False)):
        g = g.assign(size_tier=pd.Categorical(g.size_tier, ["small", "medium", "large"], ordered=True)).sort_values("size_tier")
        bars = ax.barh(g.short_name, g.nominal_params_m, color=[SIZE_COLORS[str(x)] for x in g.size_tier], alpha=.92)
        for bar, value in zip(bars, g.nominal_params_m):
            ax.text(value * 1.07, bar.get_y() + bar.get_height() / 2, format_params_m(value), va="center", fontweight="bold")
        ax.set_xscale("log")
        ax.set_title(family.capitalize())
        ax.set_xlabel("Paramètres (échelle logarithmique)")
        ax.set_ylabel("")
        ax.grid(axis="x"); ax.grid(axis="y", visible=False)
        panel_label(ax, chr(65 + families.index(family)))
    fig.suptitle("Plan expérimental 3 × 3", y=1.03)
    close_figure(fig, "design_3x3_model_sizes", "Neuf modèles ; tailles affichées avec les suffixes M et B.", show)


def plot_stimuli_coverage(protocol_volume_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the four-panel coverage dashboard of the stimuli.

    Parameters
    ----------
    protocol_volume_df : pandas.DataFrame
        Single-row table returned by ``stats_utils.export_stimuli_catalog``.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    probability_domains = PAIR_DF.groupby("domain").size().sort_values()
    generation_matrix = GENERATION_PAIRS.pivot_table(index="domain", columns="task", values="pair_id",
                                                     aggfunc="count", fill_value=0)
    lexicon_sizes = pd.Series({key: len(value) for key, value in GENDER_SETS_FR.items()}).sort_values()

    fig, axes = plt.subplots(2, 2, figsize=(16, 11), constrained_layout=True)
    probability_domains.plot.barh(ax=axes[0, 0], color="#0072B2")
    axes[0, 0].set(title=f"{len(PAIR_DF)} paires probabilistes par domaine", xlabel="Nombre de paires", ylabel="")

    sns.heatmap(generation_matrix, cmap="Blues", annot=True, fmt="g", linewidths=.4,
                cbar_kws={"label": "Nombre de scénarios"}, ax=axes[0, 1])
    axes[0, 1].set(title=f"{len(GENERATION_PAIRS)} scénarios génératifs : domaines × tâches",
                   xlabel="Tâche", ylabel="Domaine")

    protocol_counts = protocol_volume_df[[
        "probability_pairs", "generation_scenarios", "lpbs_contexts", "seat_templates"
    ]].iloc[0].sort_values()
    protocol_counts.plot.barh(ax=axes[1, 0], color="#E69F00")
    axes[1, 0].set(title="Volume du protocole unique", xlabel="Nombre d'unités", ylabel="")

    lexicon_sizes.plot.barh(ax=axes[1, 1], color="#009E73")
    axes[1, 1].set(title="Couverture des lexiques WEAT/SEAT", xlabel="Nombre de termes", ylabel="")
    fig.suptitle("Couverture du protocole avant exécution", y=1.02)
    close_figure(fig, "stimuli_coverage_dashboard",
                 "Inventaire du catalogue synthétique et du protocole d'exécution unique.", show)


def plot_embedding_direct_bias(direct_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the signed projection of every occupation, one figure per tier.

    Parameters
    ----------
    direct_df : pandas.DataFrame
        Output of ``embeddings.run_direct_bias`` for the three encoders.
    show : bool, optional
        Display the figures in addition to saving them.

    Notes
    -----
    Occupations share one order across figures, so the three encoders can be
    read side by side.
    """
    if direct_df.empty:
        return
    d = model_meta(direct_df)
    order = d.groupby("occupation").abs_projection.mean().sort_values().index
    for tier, g in d.groupby("size_tier", sort=False):
        g = g.set_index("occupation").loc[order].reset_index()
        y = np.arange(len(g))
        fig, ax = plt.subplots(figsize=(10, max(7, .30 * len(g))), constrained_layout=True)
        ax.hlines(y, 0, g.gender_projection, color=SIZE_COLORS[tier], alpha=.5, lw=2)
        ax.scatter(g.gender_projection, y, color=SIZE_COLORS[tier], marker=SIZE_MARKERS[tier], s=42, zorder=3)
        ax.set_yticks(y, g.occupation)
        finish_axis(ax, zero=True)
        ax.set(title=f"Biais direct — {g.short_name.iloc[0]}", xlabel="Projection signée", ylabel="")
        close_figure(fig, f"embedding_direct_bias_{tier}",
                     "Projection signée par métier ; le signe dépend de l'orientation de la direction de genre.", show)


def plot_embedding_forest(embed_df: pd.DataFrame, show: bool = True) -> None:
    """Draw WEAT and SEAT effect sizes for two headline contrasts.

    Parameters
    ----------
    embed_df : pandas.DataFrame
        WEAT and SEAT results with bootstrap bounds.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if embed_df.empty:
        return
    e = model_meta(embed_df)
    combos = [("WEAT", "career_family"), ("SEAT", "career_family"),
              ("WEAT", "science_arts"), ("SEAT", "science_arts")]
    fig, axes = plt.subplots(2, 2, figsize=(13, 8), sharex=True, constrained_layout=True)
    for label, ax, (metric, test) in zip("ABCD", axes.flat, combos):
        g = e.query("metric == @metric and test == @test").sort_values("nominal_params_m")
        y = np.arange(len(g))
        for i, (_, r) in enumerate(g.iterrows()):
            ax.errorbar(r.effect_size, i, xerr=[[r.effect_size - r.ci_low], [r.ci_high - r.effect_size]],
                        fmt=SIZE_MARKERS[r.size_tier], color=SIZE_COLORS[r.size_tier],
                        ecolor=SIZE_COLORS[r.size_tier], capsize=4)
        ax.set_yticks(y, g.short_name)
        finish_axis(ax, zero=True)
        ax.set_title(f"{metric} — {test.replace('_', ' / ')}")
        ax.set_xlabel("Taille d'effet d (IC bootstrap 95 %)")
        panel_label(ax, label)
    fig.suptitle("Associations de genre dans les espaces d'embeddings", y=1.02)
    close_figure(fig, "embedding_weat_seat_forest",
                 "WEAT et SEAT, tailles d'effet avec intervalles bootstrap à 95 %.", show)


def plot_embedding_context_sensitivity(context_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the template-by-template spread of the SEAT effect size.

    Parameters
    ----------
    context_df : pandas.DataFrame
        Output of ``embeddings.contextual_effect_distribution``.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if context_df.empty:
        return
    c = model_meta(context_df)
    fig, ax = plt.subplots(figsize=(10.5, 5.5), constrained_layout=True)
    order = model_order("embedding")
    sns.violinplot(data=c, x="effect_size", y="short_name", order=order, inner=None, cut=0,
                   color="#B3DDF2", linewidth=.8, ax=ax)
    sns.stripplot(data=c, x="effect_size", y="short_name", order=order, hue="size_tier",
                  palette=SIZE_COLORS, size=6, jitter=.12, ax=ax)
    finish_axis(ax, zero=True)
    ax.set(title="Sensibilité de SEAT au choix du gabarit", xlabel="Taille d'effet par gabarit", ylabel="Modèle")
    if ax.legend_ is not None:
        ax.legend_.remove()
    close_figure(fig, "embedding_context_sensitivity",
                 "Distribution des tailles d'effet sur les 18 gabarits retenus.", show)


def plot_embedding_size_vs_direct_bias(direct_df: pd.DataFrame, show: bool = True) -> None:
    """Plot mean absolute projection against nominal model size.

    Parameters
    ----------
    direct_df : pandas.DataFrame
        Direct-bias projections for the three encoders.
    show : bool, optional
        Display the figure in addition to saving it.

    Notes
    -----
    Three points only, so the figure stays descriptive and no trend test is
    performed.
    """
    if direct_df.empty:
        return
    scale = (model_meta(direct_df).groupby(["short_name", "size_tier", "nominal_params_m"], as_index=False)
             .agg(mean_abs_projection=("abs_projection", "mean"), sd_abs_projection=("abs_projection", "std")))
    fig, ax = plt.subplots(figsize=(8.5, 5.5), constrained_layout=True)
    for _, r in scale.sort_values("nominal_params_m").iterrows():
        ax.errorbar(r.nominal_params_m, r.mean_abs_projection, yerr=r.sd_abs_projection,
                    fmt=SIZE_MARKERS[r.size_tier], color=SIZE_COLORS[r.size_tier], capsize=4, label=r.short_name)
        ax.annotate(r.short_name, (r.nominal_params_m, r.mean_abs_projection),
                    xytext=(6, 6), textcoords="offset points")
    ax.set_xscale("log")
    ax.set(title="Taille du modèle et amplitude moyenne du biais direct",
           xlabel="Paramètres (millions, échelle logarithmique)",
           ylabel="Projection absolue moyenne ± écart-type")
    close_figure(fig, "embedding_size_vs_direct_bias",
                 "Relation descriptive entre taille et projection absolue moyenne ; trois points seulement, sans test de tendance.", show)


def plot_embedding_all_contrasts(embed_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the six contrasts as a heatmap, then the FDR significance map.

    Parameters
    ----------
    embed_df : pandas.DataFrame
        WEAT and SEAT results carrying a ``q_value`` column.
    show : bool, optional
        Display the figures in addition to saving them.

    Warns
    -----
    UserWarning
        When no adjusted p-value is available, in which case the second map
        is skipped.
    """
    if embed_df.empty:
        return
    extended = model_meta(embed_df).copy()
    extended["contrast_metric"] = extended["metric"] + " · " + extended["test"].str.replace("_", " / ")
    order = model_order("embedding")
    matrix = extended.pivot_table(index="short_name", columns="contrast_metric",
                                  values="effect_size", aggfunc="mean").reindex(order)
    limit = symmetric_limit(matrix)
    fig, ax = plt.subplots(figsize=(18, 5.5), constrained_layout=True)
    sns.heatmap(matrix, cmap="vlag", center=0, vmin=-limit, vmax=limit, annot=True, fmt=".2f",
                linewidths=.5, cbar_kws={"label": "Taille d'effet signée"}, ax=ax)
    ax.set(title="Six contrastes WEAT et SEAT sur trois encodeurs", xlabel="Métrique et contraste", ylabel="Modèle")
    ax.tick_params(axis="x", rotation=35)
    close_figure(fig, "embedding_all_contrasts_heatmap",
                 "Effets signés sur six contrastes ; aucune agrégation en score unique.", show)

    require_columns(extended, ["short_name", "contrast_metric", "q_value"], "résultats WEAT/SEAT")
    significance = extended.pivot_table(index="short_name", columns="contrast_metric",
                                        values="q_value", aggfunc="min").reindex(order)
    if not significance.notna().any().any():
        warnings.warn("Aucune valeur q valide : la carte FDR n'est pas produite.")
        return
    fig, ax = plt.subplots(figsize=(18, 4.8), constrained_layout=True)
    sns.heatmap(-np.log10(significance.clip(lower=1e-12)), cmap="crest", annot=significance, fmt=".3f",
                mask=significance.isna(), linewidths=.5, cbar_kws={"label": "−log10(p ajustée)"}, ax=ax)
    ax.set(title="Valeurs p ajustées des tests d'association", xlabel="Métrique et contraste", ylabel="Modèle")
    ax.tick_params(axis="x", rotation=35)
    close_figure(fig, "embedding_fdr_significance_heatmap",
                 "Annotations = valeurs p corrigées FDR ; couleur = −log10(p ajustée).", show)


def forest_plot(summary: pd.DataFrame, estimate: str = "mean_delta", low: str = "ci_low",
                high: str = "ci_high", stem: str = "forest_probability", show: bool = True) -> None:
    """Draw a generic forest plot of paired estimates.

    Parameters
    ----------
    summary : pandas.DataFrame
        Table with one estimate and its bounds per model.
    estimate, low, high : str, optional
        Column names of the point estimate and its interval.
    stem : str, optional
        Output file name without extension.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if summary.empty:
        return
    d = model_meta(summary).sort_values("nominal_params_m").reset_index(drop=True)
    y = np.arange(len(d))
    fig, ax = plt.subplots(figsize=(9, max(4, .7 * len(d))), constrained_layout=True)
    for i, (_, r) in enumerate(d.iterrows()):
        ax.errorbar(r[estimate], i, xerr=[[r[estimate] - r[low]], [r[high] - r[estimate]]],
                    fmt=SIZE_MARKERS[r.size_tier], color=SIZE_COLORS[r.size_tier],
                    ecolor=SIZE_COLORS[r.size_tier], capsize=4)
    finish_axis(ax, zero=True)
    ax.set_yticks(y, d.short_name)
    ax.set_xlabel("Écart moyen homme − femme (IC bootstrap 95 %)")
    ax.set_title("Préférence probabiliste appariée")
    close_figure(fig, stem, "Écart apparié moyen et intervalle bootstrap à 95 %.", show)


def plot_probability_forests_by_metric(prob_summary: pd.DataFrame, show: bool = True) -> None:
    """Draw one forest plot per probability metric.

    Parameters
    ----------
    prob_summary : pandas.DataFrame
        Paired probability summary.
    show : bool, optional
        Display the figures in addition to saving them.

    Notes
    -----
    Metrics get separate panels so that pseudo-log-likelihood and causal
    log-probability, which do not share a scale, are never superimposed.
    """
    if prob_summary.empty:
        return
    for metric, panel in prob_summary.groupby("metric"):
        forest_plot(panel, stem=f"forest_{metric}", show=show)


def plot_mlm_three_metrics(prob_summary: pd.DataFrame, show: bool = True) -> None:
    """Compare PLL, AUL and AULA across the three masked models.

    Parameters
    ----------
    prob_summary : pandas.DataFrame
        Paired probability summary; only masked models are kept.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if prob_summary.empty:
        return
    p = model_meta(prob_summary.query("family == 'masked_lm'"))
    metrics = [m for m in ["mean_PLL", "AUL", "AULA"] if m in set(p.metric)]
    if not metrics:
        return
    fig, axes = plt.subplots(1, len(metrics), figsize=(5.2 * len(metrics), 5), sharey=True, constrained_layout=True)
    axes = np.atleast_1d(axes)
    for label, ax, metric in zip("ABC", axes, metrics):
        g = p.query("metric == @metric").sort_values("nominal_params_m")
        y = np.arange(len(g))
        for i, (_, r) in enumerate(g.iterrows()):
            ax.errorbar(r.mean_delta, i, xerr=[[r.mean_delta - r.ci_low], [r.ci_high - r.mean_delta]],
                        fmt=SIZE_MARKERS[r.size_tier], color=SIZE_COLORS[r.size_tier], capsize=4)
        ax.set_yticks(y, g.short_name)
        finish_axis(ax, zero=True)
        ax.set_title(metric)
        ax.set_xlabel("Écart homme − femme")
        panel_label(ax, label)
    fig.suptitle("Trois métriques probabilistes sur trois modèles masqués", y=1.03)
    close_figure(fig, "probability_mlm_three_metrics_forest",
                 "PLL, AUL et AULA : écarts appariés et IC bootstrap à 95 %.", show)


def plot_lpbs_heatmap(lpbs_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the corrected LPBS by activity, wording and model.

    Parameters
    ----------
    lpbs_df : pandas.DataFrame
        Output of ``probability.run_lpbs``; invalid rows are excluded.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if lpbs_df.empty:
        return
    valid = model_meta(lpbs_df.query("valid")).copy()
    split = valid.domain.str.rsplit("_", n=1, expand=True)
    valid["activity"] = split[0].str.replace("_", " ")
    valid["formulation"] = split[1].map({"action": "Action", "quality": "Quality"})
    order = model_order("probability")
    activity_order = valid.groupby("activity").lpbs.mean().sort_values().index
    lim = symmetric_limit(valid.lpbs)
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 9.5), sharey=True, constrained_layout=True)
    for label, ax, name in zip("ABC", axes, order):
        heat = (valid.query("short_name == @name")
                .pivot_table(index="activity", columns="formulation", values="lpbs", aggfunc="mean")
                .reindex(activity_order))
        sns.heatmap(
            heat, cmap="vlag", center=0, vmin=-lim, vmax=lim, annot=True, fmt=".2f",
            annot_kws={"fontsize": 9, "fontweight": "bold"}, linewidths=.8, linecolor="white",
            cbar=ax is axes[-1], cbar_kws={"label": "LPBS corrigé", "shrink": .72}, ax=ax,
        )
        size = MODEL_REGISTRY.set_index("short_name").loc[name, "size_label"]
        ax.set(title=f"{name} · {size}", xlabel="Formulation", ylabel="Activité" if ax is axes[0] else "")
        ax.tick_params(axis="x", rotation=0); ax.tick_params(axis="y", rotation=0)
        panel_label(ax, label)
    fig.suptitle("LPBS par activité, formulation et modèle", y=1.02)
    close_figure(fig, "probability_lpbs_heatmap",
                 "Trois panneaux ; une activité par ligne et deux formulations par colonne.", show)


def plot_pll_item_distribution(mlm_pair_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the item-level spread of the pseudo-log-likelihood gap.

    Parameters
    ----------
    mlm_pair_df : pandas.DataFrame
        Item-level masked-model scores.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if mlm_pair_df.empty:
        return
    item = model_meta(mlm_pair_df.query("score_type == 'mean_PLL'"))
    fig, ax = plt.subplots(figsize=(11, 5.8), constrained_layout=True)
    order = model_order("probability")
    sns.boxplot(data=item, x="delta_male_minus_female", y="short_name", order=order,
                color="#DCEAF4", showfliers=False, ax=ax)
    sns.stripplot(data=item, x="delta_male_minus_female", y="short_name", order=order,
                  hue="domain", size=6, jitter=.16, ax=ax)
    finish_axis(ax, zero=True)
    ax.set(title="Distribution des écarts de pseudo-log-vraisemblance",
           xlabel="PLL moyenne : homme − femme", ylabel="Modèle")
    ax.legend(title="Domaine", bbox_to_anchor=(1.02, 1), loc="upper left", frameon=False)
    close_figure(fig, "probability_pll_item_distribution",
                 "Chaque point correspond à une paire contrefactuelle ; boîte = distribution inter-stimuli.", show)


def plot_male_preference_rate(prob_summary: pd.DataFrame, show: bool = True) -> None:
    """Draw the share of pairs where the male wording scores higher.

    Parameters
    ----------
    prob_summary : pandas.DataFrame
        Paired probability summary; the masked mean PLL rows are used.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if prob_summary.empty:
        return
    pref = model_meta(prob_summary.query("family == 'masked_lm' and metric == 'mean_PLL'"))
    fig, ax = plt.subplots(figsize=(8.5, 4.8), constrained_layout=True)
    for _, r in pref.iterrows():
        ax.scatter(100 * r.pct_male_preferred, r.short_name, s=70,
                   marker=SIZE_MARKERS[r.size_tier], color=SIZE_COLORS[r.size_tier])
    ax.axvline(50, color="#333333", lw=.9, ls="--")
    ax.set_xlim(0, 100)
    finish_axis(ax, percent=True)
    ax.set(title="Part des paires où la formulation masculine est préférée",
           xlabel="Paires avec score masculin supérieur", ylabel="Modèle")
    close_figure(fig, "probability_male_preference_rate",
                 "Taux descriptif sur les paires contrefactuelles ; ligne pointillée = parité.", show)


def plot_probability_diagnostics(mlm_pair_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the domain breakdown and the tokenisation diagnostic.

    Parameters
    ----------
    mlm_pair_df : pandas.DataFrame
        Item-level masked-model scores.
    show : bool, optional
        Display the figures in addition to saving them.

    Notes
    -----
    The second panel checks whether a gap merely tracks a difference in
    sub-token counts between the two wordings.
    """
    if mlm_pair_df.empty:
        return
    pll_items = model_meta(mlm_pair_df.query("score_type == 'mean_PLL'")).copy()
    order = model_order("probability")
    domain_order = pll_items.groupby("domain").delta_male_minus_female.mean().sort_values().index

    fig, axes = plt.subplots(1, 3, figsize=(16, 8), sharey=True, constrained_layout=True)
    for label, ax, name in zip("ABC", axes, order):
        g = (pll_items.query("short_name == @name").groupby("domain", as_index=False)
             .delta_male_minus_female.mean().set_index("domain").reindex(domain_order).reset_index())
        colors = np.where(g.delta_male_minus_female >= 0, GROUP_COLORS["male"], GROUP_COLORS["female"])
        ax.barh(g.domain.str.replace("_", " "), g.delta_male_minus_female, color=colors)
        ax.axvline(0, color="#333333", lw=.9)
        size = MODEL_REGISTRY.set_index("short_name").loc[name, "size_label"]
        ax.set(title=f"{name} · {size}", xlabel="PLL moyenne : homme − femme",
               ylabel="Domaine" if ax is axes[0] else "")
        ax.grid(axis="x"); ax.grid(axis="y", visible=False)
        panel_label(ax, label)
    fig.suptitle("Préférence probabiliste par domaine professionnel", y=1.02)
    close_figure(fig, "probability_domain_pll_bars",
                 "Barres signées par domaine ; bleu = positif, rose = négatif.", show)

    pll_items["token_gap"] = pll_items["male_tokens"] - pll_items["female_tokens"]
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.8), sharex=True, sharey=True, constrained_layout=True)
    for label, ax, name in zip("ABC", axes, order):
        group = pll_items.query("short_name == @name")
        sns.scatterplot(data=group, x="token_gap", y="delta_male_minus_female", hue="domain",
                        palette="tab20", alpha=.75, s=45, legend=False, ax=ax)
        ax.axhline(0, color="#333333", lw=.8)
        ax.axvline(0, color="#777777", lw=.8, ls="--")
        ax.set(title=name, xlabel="Jetons : homme − femme",
               ylabel="PLL : homme − femme" if ax is axes[0] else "")
        panel_label(ax, label)
    fig.suptitle("Diagnostic de tokenisation", y=1.03)
    close_figure(fig, "probability_tokenization_diagnostic",
                 "Relation descriptive entre écarts de tokenisation et de PLL.", show)


def plot_generation_task_heatmaps(gen_df: pd.DataFrame, show: bool = True) -> None:
    """Draw six screening metrics broken down by generation task.

    Parameters
    ----------
    gen_df : pandas.DataFrame
        Scored generations.
    show : bool, optional
        Display the figure in addition to saving it.

    Notes
    -----
    Each panel keeps its own colour scale; the metrics are never averaged
    together.
    """
    if gen_df.empty:
        return
    order = model_order("generation")
    metric_panels = ["sentiment_proxy", "agency_communality", "rate_leadership",
                     "rate_care", "rate_money", "rate_uncertainty"]
    fig, axes = plt.subplots(2, 3, figsize=(18, 9), constrained_layout=True)
    for label, ax, metric in zip("ABCDEF", axes.flat, metric_panels):
        pivot = gen_df.pivot_table(index=["model_id", "pair_id", "task", "seed"], columns="group",
                                   values=metric, aggfunc="first").dropna()
        pivot["delta"] = pivot["male"] - pivot["female"]
        domain_task = pivot.reset_index().groupby(["model_id", "task"], as_index=False).delta.mean()
        domain_task = model_meta(domain_task)
        matrix = domain_task.pivot(index="short_name", columns="task", values="delta").reindex(order)
        limit = symmetric_limit(matrix)
        sns.heatmap(matrix, cmap="vlag", center=0, vmin=-limit, vmax=limit, annot=True, fmt=".2f",
                    linewidths=.35, cbar=False, ax=ax)
        ax.set(title=metric.replace("rate_", "").replace("_", " ").capitalize(), xlabel="", ylabel="")
        ax.tick_params(axis="x", rotation=35)
        panel_label(ax, label)
    fig.suptitle("Écarts masculin − féminin par tâche de génération", y=1.02)
    close_figure(fig, "generation_task_metric_heatmaps",
                 "Six métriques de dépistage ventilées par tâche ; aucune moyenne inter-métriques.", show)


def plot_generation_lexical_associations(gen_df: pd.DataFrame, show: bool = True) -> None:
    """Compare three lexicon rates between male and female prompts.

    Parameters
    ----------
    gen_df : pandas.DataFrame
        Scored generations.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if gen_df.empty:
        return
    gm = model_meta(gen_df)
    long = gm.melt(id_vars=["short_name", "size_tier", "pair_id", "group", "seed"],
                   value_vars=["rate_leadership", "rate_care", "rate_competence"],
                   var_name="lexicon", value_name="occurrences_per_100_words")
    order = model_order("generation")
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True, constrained_layout=True)
    for label, ax, name in zip("ABC", axes, order):
        g = long.query("short_name == @name")
        sns.pointplot(data=g, x="lexicon", y="occurrences_per_100_words", hue="group", palette=GROUP_COLORS,
                      markers=["o", "s"], linestyles=["-", "--"], dodge=.2, errorbar=("ci", 95),
                      seed=SEED, ax=ax)
        ax.set_title(name); ax.set_xlabel("")
        ax.set_ylabel("Occurrences pour 100 mots" if ax is axes[0] else "")
        ax.tick_params(axis="x", rotation=20)
        panel_label(ax, label)
        if ax is not axes[-1]:
            ax.legend_.remove()
        else:
            ax.legend(title="Prompt", labels=["Masculin", "Féminin"], frameon=False)
    fig.suptitle("Associations lexicales selon le genre du prompt et le modèle", y=1.03)
    close_figure(fig, "generation_lexical_associations_3models",
                 "Moyennes et IC bootstrap seaborn à 95 % sur les sorties répétées.", show)


def plot_semantic_divergence_distribution(sim_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the distribution of counterfactual semantic divergence.

    Parameters
    ----------
    sim_df : pandas.DataFrame
        Paired similarity table.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if sim_df.empty:
        return
    sm = model_meta(sim_df)
    order = model_order("generation")
    fig, ax = plt.subplots(figsize=(10.5, 5.5), constrained_layout=True)
    sns.violinplot(data=sm, x="semantic_divergence", y="short_name", order=order, inner=None, cut=0,
                   color="#CFE8DC", linewidth=.8, ax=ax)
    sns.stripplot(data=sm, x="semantic_divergence", y="short_name", order=order, hue="domain",
                  size=5.5, jitter=.15, ax=ax)
    ax.set(title="Divergence sémantique entre prompts contrefactuels",
           xlabel="1 − similarité cosinus", ylabel="Modèle")
    ax.legend(title="Domaine", bbox_to_anchor=(1.02, 1), loc="upper left", frameon=False)
    close_figure(fig, "generation_semantic_divergence_distribution",
                 "Distribution par domaine et graine de la divergence entre sorties appariées.", show)


def plot_generation_effects_forest(gen_summary: pd.DataFrame, show: bool = True) -> None:
    """Draw the paired generation effects for four headline metrics.

    Parameters
    ----------
    gen_summary : pandas.DataFrame
        Paired generation summary.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if gen_summary.empty:
        return
    gs = model_meta(gen_summary)
    selected = ["rate_leadership", "rate_care", "rate_competence", "gender_polarity"]
    fig, axes = plt.subplots(2, 2, figsize=(13, 8), sharey=True, constrained_layout=True)
    for label, ax, metric in zip("ABCD", axes.flat, selected):
        g = gs.query("metric == @metric").sort_values("nominal_params_m")
        y = np.arange(len(g))
        for i, (_, r) in enumerate(g.iterrows()):
            ax.errorbar(r.mean_delta, i, xerr=[[r.mean_delta - r.ci_low], [r.ci_high - r.mean_delta]],
                        fmt=SIZE_MARKERS[r.size_tier], color=SIZE_COLORS[r.size_tier], capsize=4)
        ax.set_yticks(y, g.short_name)
        finish_axis(ax, zero=True)
        ax.set_title(metric.replace("rate_", "").replace("_", " ").capitalize())
        ax.set_xlabel("Écart prompt masculin − féminin")
        panel_label(ax, label)
    fig.suptitle("Effets appariés dans les générations", y=1.02)
    close_figure(fig, "generation_effects_forest_4metrics",
                 "Écarts moyens entre prompts appariés avec IC bootstrap à 95 %.", show)


def plot_seed_stability(gen_df: pd.DataFrame, show: bool = True) -> None:
    """Draw mean gender polarity seed by seed.

    Parameters
    ----------
    gen_df : pandas.DataFrame
        Scored generations.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if gen_df.empty:
        return
    seed_means = model_meta(gen_df).groupby(["short_name", "size_tier", "seed", "group"], as_index=False).gender_polarity.mean()
    order = model_order("generation")
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.8), sharey=True, constrained_layout=True)
    for label, ax, name in zip("ABC", axes, order):
        g = seed_means.query("short_name == @name")
        sns.lineplot(data=g, x="seed", y="gender_polarity", hue="group", style="group", palette=GROUP_COLORS,
                     markers=True, dashes={"male": "", "female": (3, 2)}, ax=ax)
        ax.axhline(0, color="#333333", lw=.8)
        ax.set_title(name); ax.set_xlabel("Graine")
        ax.set_ylabel("Polarité de genre" if ax is axes[0] else "")
        panel_label(ax, label)
        if ax is not axes[-1]:
            ax.legend_.remove()
        else:
            ax.legend(title="Prompt", frameon=False)
    fig.suptitle("Stabilité de la polarité de genre selon la graine", y=1.03)
    close_figure(fig, "generation_seed_stability",
                 "Polarité lexicale moyenne par graine ; le protocole utilise quatre graines.", show)


def plot_cooccurrence_polarity(gen_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the mean COBS scores and gender polarity per model.

    Parameters
    ----------
    gen_df : pandas.DataFrame
        Scored generations.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if gen_df.empty:
        return
    order = model_order("generation")
    co = model_meta(gen_df).groupby("short_name")[["cobs_leadership", "cobs_science", "gender_polarity"]].mean()
    co = co.reindex(order)
    lim = symmetric_limit(co)
    fig, ax = plt.subplots(figsize=(8.5, 4.8), constrained_layout=True)
    sns.heatmap(co, cmap="vlag", center=0, vmin=-lim, vmax=lim, annot=True, fmt=".2f", linewidths=.5,
                cbar_kws={"label": "Score signé"}, ax=ax)
    ax.set(title="COBS et polarité de genre par modèle", xlabel="Métrique", ylabel="Modèle")
    close_figure(fig, "generation_cooccurrence_polarity_heatmap",
                 "Scores lexicaux signés ; valeurs positives = davantage de termes masculins.", show)


def plot_domain_divergence(sim_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the mean counterfactual divergence by domain.

    Parameters
    ----------
    sim_df : pandas.DataFrame
        Paired similarity table.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if sim_df.empty:
        return
    order = model_order("generation")
    dom = (model_meta(sim_df).pivot_table(index="short_name", columns="domain",
                                          values="semantic_divergence", aggfunc="mean").reindex(order))
    fig, ax = plt.subplots(figsize=(10, 4.6), constrained_layout=True)
    sns.heatmap(dom, cmap="mako", annot=True, fmt=".3f", linewidths=.5,
                cbar_kws={"label": "Divergence moyenne"}, ax=ax)
    ax.set(title="Divergence contrefactuelle moyenne par domaine", xlabel="Domaine", ylabel="Modèle")
    close_figure(fig, "generation_domain_divergence_heatmap",
                 "Moyenne par domaine de 1 − similarité cosinus entre sorties appariées.", show)


def plot_output_length_slopegraph(gen_df: pd.DataFrame, show: bool = True) -> None:
    """Draw mean response length as a slopegraph between prompt groups.

    Parameters
    ----------
    gen_df : pandas.DataFrame
        Scored generations.
    show : bool, optional
        Display the figure in addition to saving it.
    """
    if gen_df.empty:
        return
    length = model_meta(gen_df).groupby(["short_name", "group"], as_index=False).word_count.mean()
    female_order = length.query("group == 'female'").sort_values("word_count").short_name.tolist()
    offsets = dict(zip(female_order, np.linspace(-12, 12, len(female_order))))
    fig, ax = plt.subplots(figsize=(9.5, 5.4), constrained_layout=True)
    for name, g in length.groupby("short_name"):
        m = float(g.loc[g.group == "male", "word_count"].iloc[0])
        f = float(g.loc[g.group == "female", "word_count"].iloc[0])
        ax.plot([0, 1], [m, f], color="#888888", lw=1.5)
        ax.scatter([0, 1], [m, f], c=[GROUP_COLORS["male"], GROUP_COLORS["female"]], s=55)
        ax.annotate(name, (1, f), xytext=(10, offsets[name]), textcoords="offset points", va="center")
    ax.set_xticks([0, 1], ["Prompt masculin", "Prompt féminin"])
    ax.set_xlim(-.15, 1.52)
    ax.set(title="Longueur moyenne des réponses appariées", ylabel="Nombre moyen de mots", xlabel="")
    close_figure(fig, "generation_output_length_slopegraph",
                 "Longueur moyenne par groupe de prompts ; chaque segment représente un modèle.", show)


def plot_performance(perf_df: pd.DataFrame, show: bool = True) -> None:
    """Draw throughput, latency, memory, then the latency-memory trade-off.

    Parameters
    ----------
    perf_df : pandas.DataFrame
        Output of ``text_generation.performance_summary``.
    show : bool, optional
        Display the figures in addition to saving them.

    Notes
    -----
    Layer placement and batch size must be checked before reading these
    panels as a size effect.
    """
    if perf_df.empty:
        return
    perf = model_meta(perf_df).sort_values("nominal_params_m")
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True, constrained_layout=True)
    specs = [("median_tokens_s", "Débit médian", "tokens/s"),
             ("median_latency_s", "Latence médiane", "secondes"),
             ("peak_gpu_mb", "Pic mémoire GPU", "MiB")]
    for label, ax, (col, title, unit) in zip("ABC", axes, specs):
        sns.barplot(data=perf, y="short_name", x=col, hue="size_tier", palette=SIZE_COLORS, dodge=False, ax=ax)
        ax.set(title=title, xlabel=unit, ylabel="")
        if ax.legend_ is not None:
            ax.legend_.remove()
        panel_label(ax, label)
    fig.suptitle("Coût d'inférence des trois modèles génératifs", y=1.03)
    close_figure(fig, "performance_models_three_panels",
                 "Débit, latence et mémoire observés ; contrôler le placement des couches et la taille des lots avant comparaison.", show)

    fig, ax = plt.subplots(figsize=(8.5, 5.8), constrained_layout=True)
    for _, r in perf.iterrows():
        ax.scatter(r.median_latency_s, r.peak_gpu_mb, s=50 + 55 * np.log10(max(r.nominal_params_m, 10)),
                   marker=SIZE_MARKERS[r.size_tier], color=SIZE_COLORS[r.size_tier])
        ax.annotate(r.short_name, (r.median_latency_s, r.peak_gpu_mb), xytext=(7, 6), textcoords="offset points")
    ax.set(title="Compromis latence–mémoire", xlabel="Latence médiane (s)", ylabel="Pic mémoire GPU (MiB)")
    close_figure(fig, "performance_latency_memory_pareto",
                 "Chaque point est un modèle ; la taille du marqueur augmente avec le nombre nominal de paramètres.", show)


def plot_synthesis_heatmaps(synthesis_df: pd.DataFrame, show: bool = True) -> None:
    """Draw one normalised synthesis heatmap per family.

    Parameters
    ----------
    synthesis_df : pandas.DataFrame
        Output of ``stats_utils.build_synthesis_table``.
    show : bool, optional
        Display the figures in addition to saving them.

    Notes
    -----
    Z-scores are computed within each metric, so no cell can be read as a
    global bias score.
    """
    if synthesis_df.empty:
        return
    syn = model_meta(synthesis_df)
    families = [f for f in ["embedding", "probability", "generation"] if f in set(syn.category)]
    for family in families:
        g = syn.query("category == @family")
        heat = g.pivot_table(index="short_name", columns="metric", values="z", aggfunc="mean")
        heat = heat.reindex(model_order(family))
        width = max(8, 1.05 * len(heat.columns) + 3)
        fig, ax = plt.subplots(figsize=(width, 4.6), constrained_layout=True)
        sns.heatmap(heat, center=0, cmap="vlag", annot=True, fmt=".2f", linewidths=.5,
                    cbar_kws={"label": "z-score interne à la métrique"}, ax=ax)
        ax.set(title=f"Synthèse normalisée — {family}", xlabel="Métrique", ylabel="Modèle")
        ax.tick_params(axis="x", rotation=35)
        close_figure(fig, f"synthesis_heatmap_{family}",
                     "Z-scores internes à chaque métrique ; aucun score global.", show)


def plot_conclusion_3x3(conclusion_df: pd.DataFrame, show: bool = True) -> None:
    """Draw the headline metric of each family against model size.

    Parameters
    ----------
    conclusion_df : pandas.DataFrame
        Output of ``stats_utils.build_conclusion_3x3``.
    show : bool, optional
        Display the figure in addition to saving it.

    Notes
    -----
    Panels carry different units and must not be compared with one another.
    """
    if conclusion_df.empty:
        return
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.2), constrained_layout=True)
    for label, ax, family in zip("ABC", axes, ["embedding", "probability", "generation"]):
        g = conclusion_df.query("family == @family").sort_values("nominal_params_m")
        ax.plot(g.nominal_params_m, g.estimate, color="#777777", lw=1.2, zorder=1)
        for _, r in g.iterrows():
            ax.errorbar(r.nominal_params_m, r.estimate,
                        yerr=[[r.estimate - r.ci_low], [r.ci_high - r.estimate]],
                        fmt=SIZE_MARKERS[r.size_tier], color=SIZE_COLORS[r.size_tier], capsize=4, zorder=2)
            ax.annotate(r.short_name, (r.nominal_params_m, r.estimate),
                        xytext=(5, 6), textcoords="offset points", fontsize=8.5)
        ax.set_xscale("log")
        ax.set_title(family.capitalize())
        ax.set_xlabel("Paramètres (millions, log)")
        ax.set_ylabel(g.conclusion_metric.iloc[0])
        panel_label(ax, label)
        ax.axhline(0, color="#333333", lw=.8, ls="--")
    fig.suptitle("Comparaison finale 3 × 3 : taille du modèle et métrique principale", y=1.03)
    close_figure(fig, "conclusion_3x3_size_and_bias",
                 "Un panneau par famille ; les unités ne sont pas comparées entre panneaux.", show)
