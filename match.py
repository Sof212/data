from pathlib import Path

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)


def evaluer_et_exporter_excel(
    df: pd.DataFrame,
    fichier_sortie: str = "evaluation_normalisation.xlsx",
    prediction_col: str = "normalisé",
    label_col: str = "label",
    input_col: str = "input_name",
    top_n_classes: int = 15,
    top_n_confusions: int = 15,
    ignorer_casse: bool = False,
) -> dict[str, pd.DataFrame]:
    """
    Évalue un modèle de normalisation et exporte les résultats dans Excel.

    Les métriques par classe contiennent uniquement les classes présentes
    dans la colonne label.

    Feuilles créées :
    - Dashboard
    - Par_classe
    - Erreurs
    - Confusions
    - Donnees_evaluees
    """

    # ------------------------------------------------------------------
    # 1. Validation des colonnes
    # ------------------------------------------------------------------
    colonnes_requises = {prediction_col, label_col}
    colonnes_manquantes = colonnes_requises - set(df.columns)

    if colonnes_manquantes:
        raise ValueError(
            f"Colonnes manquantes : {sorted(colonnes_manquantes)}. "
            f"Colonnes disponibles : {df.columns.tolist()}"
        )

    data = df.copy()

    # Une ligne sans label ne peut pas être évaluée.
    data = data.dropna(subset=[label_col]).copy()

    if data.empty:
        raise ValueError("Aucune ligne avec un label valide à évaluer.")

    # ------------------------------------------------------------------
    # 2. Nettoyage léger des valeurs
    # ------------------------------------------------------------------
    def nettoyer(serie: pd.Series) -> pd.Series:
        resultat = (
            serie.astype("string")
            .str.normalize("NFKC")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .replace("", pd.NA)
        )

        if ignorer_casse:
            resultat = resultat.str.casefold()

        return resultat

    y_true = nettoyer(data[label_col])

    # Les labels devenus vides après nettoyage sont supprimés.
    lignes_valides = y_true.notna()
    data = data.loc[lignes_valides].copy()
    y_true = y_true.loc[lignes_valides]

    y_pred = nettoyer(data[prediction_col])

    # Token utilisé pour considérer une prédiction manquante comme une erreur.
    token_manquant = "__PREDICTION_MANQUANTE__"

    valeurs_existantes = set(y_true.dropna().astype(str))

    while token_manquant in valeurs_existantes:
        token_manquant += "_"

    y_pred = y_pred.fillna(token_manquant)

    # ------------------------------------------------------------------
    # 3. Les vraies classes viennent uniquement de label
    # ------------------------------------------------------------------
    classes = sorted(y_true.unique().tolist())

    data["label_evalue"] = y_true.values
    data["prediction_evaluee"] = y_pred.values
    data["correct"] = y_true.eq(y_pred).values

    # ------------------------------------------------------------------
    # 4. Métriques par classe
    # ------------------------------------------------------------------
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=classes,
        average=None,
        zero_division=0,
    )

    nombre_predictions = y_pred.value_counts()
    nombre_correct = (
        data.groupby("label_evalue", dropna=False)["correct"]
        .sum()
        .astype(int)
    )

    metrics_par_classe = pd.DataFrame({
        "classe": classes,
        "support": support.astype(int),
        "nombre_predictions": [
            int(nombre_predictions.get(classe, 0))
            for classe in classes
        ],
        "nombre_correct": [
            int(nombre_correct.get(classe, 0))
            for classe in classes
        ],
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
    })

    metrics_par_classe["nombre_erreurs"] = (
        metrics_par_classe["support"]
        - metrics_par_classe["nombre_correct"]
    )

    metrics_par_classe["taux_erreur"] = (
        1 - metrics_par_classe["recall"]
    )

    metrics_par_classe = metrics_par_classe.sort_values(
        by=["support", "f1_score"],
        ascending=[False, True],
    ).reset_index(drop=True)

    # ------------------------------------------------------------------
    # 5. Métriques globales
    # ------------------------------------------------------------------
    precision_micro, recall_micro, f1_micro, _ = (
        precision_recall_fscore_support(
            y_true,
            y_pred,
            average="micro",
            zero_division=0,
        )
    )

    # Macro et weighted calculés uniquement sur les vraies classes de label.
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

    accuracy = accuracy_score(y_true, y_pred)
    nombre_correct_global = int(y_true.eq(y_pred).sum())
    nombre_erreurs_global = int(y_true.ne(y_pred).sum())

    predictions_hors_classes = ~y_pred.isin(classes)

    metrics_globales = {
        "nombre_observations": len(y_true),
        "nombre_classes_label": len(classes),
        "nombre_correct": nombre_correct_global,
        "nombre_erreurs": nombre_erreurs_global,
        "accuracy": accuracy,
        "taux_erreur": 1 - accuracy,
        "precision_micro": precision_micro,
        "recall_micro": recall_micro,
        "f1_micro": f1_micro,
        "precision_macro": precision_macro,
        "recall_macro": recall_macro,
        "f1_macro": f1_macro,
        "precision_weighted": precision_weighted,
        "recall_weighted": recall_weighted,
        "f1_weighted": f1_weighted,
        "nombre_predictions_hors_classes": int(
            predictions_hors_classes.sum()
        ),
        "taux_predictions_hors_classes": float(
            predictions_hors_classes.mean()
        ),
    }

    metrics_globales_df = pd.DataFrame({
        "metrique": metrics_globales.keys(),
        "valeur": metrics_globales.values(),
    })

    # ------------------------------------------------------------------
    # 6. Erreurs détaillées
    # ------------------------------------------------------------------
    colonnes_erreurs = []

    if input_col in data.columns:
        colonnes_erreurs.append(input_col)

    colonnes_erreurs.extend([
        label_col,
        prediction_col,
        "label_evalue",
        "prediction_evaluee",
    ])

    erreurs = (
        data.loc[~data["correct"], colonnes_erreurs]
        .reset_index(drop=True)
    )

    # ------------------------------------------------------------------
    # 7. Confusions les plus fréquentes
    # ------------------------------------------------------------------
    if erreurs.empty:
        confusions = pd.DataFrame(columns=[
            "confusion",
            "label_reel",
            "prediction",
            "nombre_erreurs",
            "support_label",
            "part_erreurs_classe",
        ])
    else:
        confusions = (
            erreurs.groupby(
                ["label_evalue", "prediction_evaluee"],
                dropna=False,
            )
            .size()
            .reset_index(name="nombre_erreurs")
            .rename(columns={
                "label_evalue": "label_reel",
                "prediction_evaluee": "prediction",
            })
        )

        supports = y_true.value_counts()

        confusions["support_label"] = (
            confusions["label_reel"]
            .map(supports)
            .fillna(0)
            .astype(int)
        )

        confusions["part_erreurs_classe"] = (
            confusions["nombre_erreurs"]
            / confusions["support_label"]
        )

        confusions["confusion"] = (
            confusions["label_reel"].astype(str)
            + " → "
            + confusions["prediction"].astype(str)
        )

        confusions = confusions[[
            "confusion",
            "label_reel",
            "prediction",
            "nombre_erreurs",
            "support_label",
            "part_erreurs_classe",
        ]].sort_values(
            "nombre_erreurs",
            ascending=False,
        ).reset_index(drop=True)

    # ------------------------------------------------------------------
    # 8. Export Excel
    # ------------------------------------------------------------------
    chemin_sortie = Path(fichier_sortie)
    chemin_sortie.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(
        chemin_sortie,
        engine="xlsxwriter",
        engine_kwargs={
            "options": {
                "strings_to_urls": False,
                "nan_inf_to_errors": True,
            }
        },
    ) as writer:

        metrics_globales_df.to_excel(
            writer,
            sheet_name="Dashboard",
            index=False,
            startrow=3,
        )

        metrics_par_classe.to_excel(
            writer,
            sheet_name="Par_classe",
            index=False,
        )

        erreurs.to_excel(
            writer,
            sheet_name="Erreurs",
            index=False,
        )

        confusions.to_excel(
            writer,
            sheet_name="Confusions",
            index=False,
        )

        data.to_excel(
            writer,
            sheet_name="Donnees_evaluees",
            index=False,
        )

        workbook = writer.book

        dashboard = writer.sheets["Dashboard"]
        ws_classes = writer.sheets["Par_classe"]
        ws_erreurs = writer.sheets["Erreurs"]
        ws_confusions = writer.sheets["Confusions"]
        ws_data = writer.sheets["Donnees_evaluees"]

        # --------------------------------------------------------------
        # Formats
        # --------------------------------------------------------------
        format_titre = workbook.add_format({
            "bold": True,
            "font_size": 20,
            "font_color": "white",
            "bg_color": "#1F4E78",
            "align": "center",
            "valign": "vcenter",
        })

        format_header = workbook.add_format({
            "bold": True,
            "font_color": "white",
            "bg_color": "#4472C4",
            "border": 1,
            "align": "center",
            "valign": "vcenter",
        })

        format_entier = workbook.add_format({
            "num_format": "#,##0",
            "border": 1,
        })

        format_pourcentage = workbook.add_format({
            "num_format": "0.00%",
            "border": 1,
        })

        format_texte = workbook.add_format({
            "border": 1,
        })

        format_note = workbook.add_format({
            "italic": True,
            "font_color": "#666666",
        })

        # --------------------------------------------------------------
        # Dashboard
        # --------------------------------------------------------------
        dashboard.merge_range(
            "A1:H2",
            "Évaluation du modèle de normalisation",
            format_titre,
        )

        dashboard.write(
            "A3",
            "Les classes affichées proviennent uniquement de la colonne label.",
            format_note,
        )

        dashboard.set_row(0, 28)
        dashboard.set_column("A:A", 36)
        dashboard.set_column("B:B", 18)
        dashboard.set_column("D:L", 13)

        dashboard.set_row(3, 22, format_header)

        metriques_pourcentage = {
            "accuracy",
            "taux_erreur",
            "precision_micro",
            "recall_micro",
            "f1_micro",
            "precision_macro",
            "recall_macro",
            "f1_macro",
            "precision_weighted",
            "recall_weighted",
            "f1_weighted",
            "taux_predictions_hors_classes",
        }

        # Mise en forme des valeurs du dashboard.
        for index, ligne in metrics_globales_df.iterrows():
            ligne_excel = 4 + index

            if ligne["metrique"] in metriques_pourcentage:
                dashboard.write_number(
                    ligne_excel,
                    1,
                    float(ligne["valeur"]),
                    format_pourcentage,
                )
            else:
                dashboard.write_number(
                    ligne_excel,
                    1,
                    float(ligne["valeur"]),
                    format_entier,
                )

            dashboard.write(
                ligne_excel,
                0,
                ligne["metrique"],
                format_texte,
            )

        # Données du graphique correct/erreur, masquées à droite.
        dashboard.write_row(
            "N2",
            ["statut", "nombre"],
            format_header,
        )
        dashboard.write_row(
            "N3",
            ["Correct", nombre_correct_global],
        )
        dashboard.write_row(
            "N4",
            ["Erreur", nombre_erreurs_global],
        )
        dashboard.set_column("N:O", None, None, {"hidden": True})

        # --------------------------------------------------------------
        # Format des feuilles de données
        # --------------------------------------------------------------
        feuilles = [
            (ws_classes, metrics_par_classe),
            (ws_erreurs, erreurs),
            (ws_confusions, confusions),
            (ws_data, data),
        ]

        for worksheet, dataframe in feuilles:
            worksheet.freeze_panes(1, 0)
            worksheet.autofilter(
                0,
                0,
                max(len(dataframe), 1),
                max(len(dataframe.columns) - 1, 0),
            )

            worksheet.set_row(0, 25, format_header)

            for colonne_index, colonne in enumerate(dataframe.columns):
                longueur_max = max(
                    len(str(colonne)),
                    dataframe[colonne]
                    .astype(str)
                    .str.len()
                    .max()
                    if not dataframe.empty else 0,
                )

                largeur = min(max(longueur_max + 2, 12), 45)
                worksheet.set_column(
                    colonne_index,
                    colonne_index,
                    largeur,
                )

        # Colonnes pourcentage de Par_classe.
        if not metrics_par_classe.empty:
            ws_classes.set_column("E:G", 13, format_pourcentage)
            ws_classes.set_column("I:I", 13, format_pourcentage)

            ws_classes.conditional_format(
                1,
                4,
                len(metrics_par_classe),
                6,
                {
                    "type": "3_color_scale",
                    "min_color": "#F8696B",
                    "mid_color": "#FFEB84",
                    "max_color": "#63BE7B",
                },
            )

        if not confusions.empty:
            ws_confusions.set_column(
                "F:F",
                18,
                format_pourcentage,
            )

        # Coloration des prédictions correctes/incorrectes.
        if not data.empty:
            colonne_correct = data.columns.get_loc("correct")

            ws_data.conditional_format(
                1,
                colonne_correct,
                len(data),
                colonne_correct,
                {
                    "type": "cell",
                    "criteria": "equal to",
                    "value": True,
                    "format": workbook.add_format({
                        "bg_color": "#C6EFCE",
                        "font_color": "#006100",
                    }),
                },
            )

            ws_data.conditional_format(
                1,
                colonne_correct,
                len(data),
                colonne_correct,
                {
                    "type": "cell",
                    "criteria": "equal to",
                    "value": False,
                    "format": workbook.add_format({
                        "bg_color": "#FFC7CE",
                        "font_color": "#9C0006",
                    }),
                },
            )

        # --------------------------------------------------------------
        # Graphique 1 : métriques par classe
        # --------------------------------------------------------------
        nombre_classes_graphique = min(
            top_n_classes,
            len(metrics_par_classe),
        )

        if nombre_classes_graphique > 0:
            graphique_classes = workbook.add_chart({
                "type": "bar",
                "subtype": "clustered",
            })

            for nom, colonne, couleur in [
                ("Précision", 4, "#4472C4"),
                ("Recall", 5, "#70AD47"),
                ("F1-score", 6, "#ED7D31"),
            ]:
                graphique_classes.add_series({
                    "name": nom,
                    "categories": [
                        "Par_classe",
                        1,
                        0,
                        nombre_classes_graphique,
                        0,
                    ],
                    "values": [
                        "Par_classe",
                        1,
                        colonne,
                        nombre_classes_graphique,
                        colonne,
                    ],
                    "fill": {"color": couleur},
                    "border": {"none": True},
                })

            graphique_classes.set_title({
                "name": f"Métriques des {nombre_classes_graphique} classes "
                        "les plus représentées"
            })
            graphique_classes.set_x_axis({
                "name": "Score",
                "min": 0,
                "max": 1,
                "num_format": "0%",
                "major_gridlines": {
                    "visible": True,
                    "line": {"color": "#D9E2F3"},
                },
            })
            graphique_classes.set_y_axis({
                "name": "Classe",
                "reverse": True,
            })
            graphique_classes.set_legend({
                "position": "bottom"
            })
            graphique_classes.set_style(10)
            graphique_classes.set_size({
                "width": 780,
                "height": 430,
            })

            dashboard.insert_chart(
                "D4",
                graphique_classes,
            )

        # --------------------------------------------------------------
        # Graphique 2 : correct vs erreur
        # --------------------------------------------------------------
        graphique_erreurs = workbook.add_chart({
            "type": "doughnut"
        })

        graphique_erreurs.add_series({
            "name": "Résultats",
            "categories": ["Dashboard", 2, 13, 3, 13],
            "values": ["Dashboard", 2, 14, 3, 14],
            "points": [
                {"fill": {"color": "#70AD47"}},
                {"fill": {"color": "#C00000"}},
            ],
            "data_labels": {
                "percentage": True,
                "category": True,
                "leader_lines": True,
            },
        })

        graphique_erreurs.set_title({
            "name": "Répartition correct / erreur"
        })
        graphique_erreurs.set_hole_size(55)
        graphique_erreurs.set_legend({
            "position": "bottom"
        })
        graphique_erreurs.set_style(10)
        graphique_erreurs.set_size({
            "width": 360,
            "height": 280,
        })

        ligne_donut = max(23, len(metrics_globales_df) + 7)

        dashboard.insert_chart(
            ligne_donut - 1,
            0,
            graphique_erreurs,
        )

        # --------------------------------------------------------------
        # Graphique 3 : confusions principales
        # --------------------------------------------------------------
        nombre_confusions_graphique = min(
            top_n_confusions,
            len(confusions),
        )

        if nombre_confusions_graphique > 0:
            graphique_confusions = workbook.add_chart({
                "type": "bar"
            })

            graphique_confusions.add_series({
                "name": "Nombre d'erreurs",
                "categories": [
                    "Confusions",
                    1,
                    0,
                    nombre_confusions_graphique,
                    0,
                ],
                "values": [
                    "Confusions",
                    1,
                    3,
                    nombre_confusions_graphique,
                    3,
                ],
                "fill": {"color": "#ED7D31"},
                "border": {"none": True},
                "data_labels": {"value": True},
            })

            graphique_confusions.set_title({
                "name": (
                    f"Top {nombre_confusions_graphique} "
                    "des confusions"
                )
            })
            graphique_confusions.set_x_axis({
                "name": "Nombre d'erreurs",
                "major_gridlines": {
                    "visible": True,
                    "line": {"color": "#D9E2F3"},
                },
            })
            graphique_confusions.set_y_axis({
                "reverse": True,
            })
            graphique_confusions.set_legend({
                "none": True
            })
            graphique_confusions.set_style(10)
            graphique_confusions.set_size({
                "width": 780,
                "height": 430,
            })

            dashboard.insert_chart(
                "D28",
                graphique_confusions,
            )

        dashboard.freeze_panes(3, 0)

    print(f"Rapport Excel créé : {chemin_sortie.resolve()}")

    return {
        "global": metrics_globales_df,
        "par_classe": metrics_par_classe,
        "erreurs": erreurs,
        "confusions": confusions,
        "donnees_evaluees": data,
    }


df = pd.read_excel("ecoles.xlsx")

resultats = evaluer_et_exporter_excel(
    df=df,
    fichier_sortie="rapport_evaluation_ecoles.xlsx",
    prediction_col="normalisé",
    label_col="label",
    input_col="input_name",
)
