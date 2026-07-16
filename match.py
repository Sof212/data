import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)


def evaluer_normalisation(
    df: pd.DataFrame,
    prediction_col: str = "normalisé",
    label_col: str = "label",
):
    """
    Évalue une classification multiclasse.

    Les métriques par classe contiennent uniquement les classes
    présentes dans la colonne label.
    """

    data = df[[prediction_col, label_col]].copy()

    # Une ligne sans vérité terrain ne peut pas être évaluée.
    data = data.dropna(subset=[label_col])

    if data.empty:
        raise ValueError("Aucune ligne valide à évaluer.")

    y_true = (
        data[label_col]
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    y_pred = (
        data[prediction_col]
        .fillna("__PREDICTION_MANQUANTE__")
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    # Les vraies classes viennent uniquement de label.
    classes = sorted(y_true.unique())

    # Métriques par vraie classe.
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=classes,
        average=None,
        zero_division=0,
    )

    metrics_par_classe = pd.DataFrame({
        "classe": classes,
        "support": support.astype(int),
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
    })

    # Métriques globales sur les vraies classes.
    precision_macro, recall_macro, f1_macro, _ = (
        precision_recall_fscore_support(
            y_true,
            y_pred,
            labels=classes,
            average="macro",
            zero_division=0,
        )
    )

    precision_weighted, recall_weighted, f1_weighted, _ = (
        precision_recall_fscore_support(
            y_true,
            y_pred,
            labels=classes,
            average="weighted",
            zero_division=0,
        )
    )

    # Micro calculé sur toutes les valeurs, y compris les prédictions
    # qui ne correspondent à aucune vraie classe.
    precision_micro, recall_micro, f1_micro, _ = (
        precision_recall_fscore_support(
            y_true,
            y_pred,
            average="micro",
            zero_division=0,
        )
    )

    metrics_globales = {
        "nombre_observations": len(y_true),
        "nombre_classes": len(classes),
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_micro": precision_micro,
        "recall_micro": recall_micro,
        "f1_micro": f1_micro,
        "precision_macro": precision_macro,
        "recall_macro": recall_macro,
        "f1_macro": f1_macro,
        "precision_weighted": precision_weighted,
        "recall_weighted": recall_weighted,
        "f1_weighted": f1_weighted,
    }

    return metrics_globales, metrics_par_classe




global_metrics, metrics_par_classe = evaluer_normalisation(df)

print("Métriques globales :")
print(pd.Series(global_metrics))

print("\nMétriques par classe :")
print(metrics_par_classe)
