import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_recall_fscore_support,
)


def evaluer_normalisation(
    df: pd.DataFrame,
    prediction_col: str = "normalisé",
    label_col: str = "label",
    input_col: str = "input_name",
    nettoyer_espaces: bool = True,
    ignorer_casse: bool = False,
) -> dict:
    """
    Évalue un modèle de normalisation de noms d'écoles.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contenant les prédictions et les labels.
    prediction_col : str
        Colonne contenant la prédiction du modèle.
    label_col : str
        Colonne contenant la vérité terrain.
    input_col : str
        Colonne contenant le nom brut. Utilisée dans le tableau des erreurs.
    nettoyer_espaces : bool
        Supprime les espaces au début/à la fin et réduit les espaces multiples.
    ignorer_casse : bool
        Compare les valeurs sans tenir compte des majuscules/minuscules.

    Returns
    -------
    dict
        {
            "global": DataFrame avec les métriques globales,
            "par_classe": DataFrame avec précision, rappel et F1 par classe,
            "erreurs": DataFrame contenant les prédictions incorrectes,
            "confusions": DataFrame des confusions les plus fréquentes
        }
    """

    colonnes_requises = {prediction_col, label_col}
    colonnes_manquantes = colonnes_requises - set(df.columns)

    if colonnes_manquantes:
        raise ValueError(
            f"Colonnes manquantes : {sorted(colonnes_manquantes)}. "
            f"Colonnes disponibles : {df.columns.tolist()}"
        )

    data = df.copy()

    # Les lignes sans vérité terrain ne peuvent pas être évaluées.
    data = data[data[label_col].notna()].copy()

    if data.empty:
        raise ValueError("Aucune ligne avec un label valide à évaluer.")

    def nettoyer(serie: pd.Series) -> pd.Series:
        serie = serie.astype("string")

        if nettoyer_espaces:
            serie = (
                serie.str.strip()
                .str.replace(r"\s+", " ", regex=True)
            )

        if ignorer_casse:
            serie = serie.str.casefold()

        return serie

    y_true = nettoyer(data[label_col])
    y_pred = nettoyer(data[prediction_col])

    # Une prédiction manquante est considérée comme une erreur.
    token_prediction_manquante = "__PREDICTION_MANQUANTE__"

    while token_prediction_manquante in set(y_true.dropna()):
        token_prediction_manquante += "_"

    y_pred = y_pred.fillna(token_prediction_manquante)

    # Exactitude globale.
    accuracy = accuracy_score(y_true, y_pred)

    metriques_globales = {
        "accuracy": accuracy,
        "error_rate": 1 - accuracy,
        "nombre_lignes": len(data),
        "nombre_correct": int((y_true == y_pred).sum()),
        "nombre_erreurs": int((y_true != y_pred).sum()),
    }

    # Moyennes micro, macro et pondérée.
    for moyenne in ("micro", "macro", "weighted"):
        precision, recall, f1, _ = precision_recall_fscore_support(
            y_true,
            y_pred,
            average=moyenne,
            zero_division=0,
        )

        metriques_globales[f"precision_{moyenne}"] = precision
        metriques_globales[f"recall_{moyenne}"] = recall
        metriques_globales[f"f1_{moyenne}"] = f1

    global_df = pd.DataFrame(
        {
            "metrique": metriques_globales.keys(),
            "valeur": metriques_globales.values(),
        }
    )

    # Précision, rappel et F1 pour chaque nom d'école.
    rapport = classification_report(
        y_true,
        y_pred,
        output_dict=True,
        zero_division=0,
    )

    lignes_par_classe = []

    for classe, valeurs in rapport.items():
        if classe in {"accuracy", "macro avg", "weighted avg"}:
            continue

        lignes_par_classe.append(
            {
                "classe": classe,
                "precision": valeurs["precision"],
                "recall": valeurs["recall"],
                "f1_score": valeurs["f1-score"],
                "support": int(valeurs["support"]),
            }
        )

    par_classe_df = (
        pd.DataFrame(lignes_par_classe)
        .sort_values(
            by=["support", "f1_score"],
            ascending=[False, True],
        )
        .reset_index(drop=True)
    )

    # Détail ligne par ligne.
    data["label_evalue"] = y_true
    data["prediction_evaluee"] = y_pred
    data["correct"] = y_true == y_pred

    colonnes_erreurs = [
        colonne
        for colonne in [
            input_col,
            label_col,
            prediction_col,
            "label_evalue",
            "prediction_evaluee",
        ]
        if colonne in data.columns
    ]

    erreurs_df = (
        data.loc[~data["correct"], colonnes_erreurs]
        .reset_index(drop=True)
    )

    # Confusions les plus fréquentes.
    confusions_df = (
        erreurs_df.groupby(
            ["label_evalue", "prediction_evaluee"],
            dropna=False,
        )
        .size()
        .reset_index(name="nombre_erreurs")
        .rename(
            columns={
                "label_evalue": "label_reel",
                "prediction_evaluee": "prediction",
            }
        )
        .sort_values("nombre_erreurs", ascending=False)
        .reset_index(drop=True)
    )

    return {
        "global": global_df,
        "par_classe": par_classe_df,
        "erreurs": erreurs_df,
        "confusions": confusions_df,
    }



df = pd.read_excel("ecoles.xlsx")

resultats = evaluer_normalisation(df)

print(resultats["global"])
print(resultats["par_classe"])
print(resultats["confusions"].head(20))
