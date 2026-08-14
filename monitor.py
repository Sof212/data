

import pandas as pd


def verifier_non_nan(df, colonne, seuil=0.50):
    """Vérifie qu'au moins `seuil` des lignes ne sont pas des NaN."""
    taux = df[colonne].notna().mean()
    return {
        "test": "valeurs non NaN",
        "colonne": colonne,
        "taux": round(float(taux), 4),
        "seuil": seuil,
        "valide": bool(taux >= seuil),
    }


def verifier_longueur(df, colonne, longueur_min=3, longueur_max=25, seuil=1.0):
    """Vérifie la part des valeurs ayant entre 3 et 25 caractères."""
    valeurs = df[colonne].dropna().astype(str).str.strip()
    longueurs_valides = valeurs.str.len().between(longueur_min, longueur_max)
    taux = longueurs_valides.mean() if len(valeurs) else 0.0

    return {
        "test": "longueur des chaînes",
        "colonne": colonne,
        "taux": round(float(taux), 4),
        "seuil": seuil,
        "valide": bool(taux >= seuil),
        "exemples_invalides": valeurs[~longueurs_valides].head(5).tolist(),
    }


def verifier_valeur_ref200(df, colonne="C", seuil=0.70):
    """Vérifie qu'au moins 70 % des lignes de C valent REF200."""
    taux = df[colonne].eq("REF200").mean()
    return {
        "test": "taux de REF200",
        "colonne": colonne,
        "taux": round(float(taux), 4),
        "seuil": seuil,
        "valide": bool(taux >= seuil),
    }


def verifier_categories(df, colonne, categories_autorisees, seuil=0.95):
    """Vérifie que les typologies prédites sont dans la liste autorisée."""
    valeurs = df[colonne].dropna()
    valeurs_valides = valeurs.isin(categories_autorisees)
    taux = valeurs_valides.mean() if len(valeurs) else 0.0

    return {
        "test": "catégories autorisées",
        "colonne": colonne,
        "taux": round(float(taux), 4),
        "seuil": seuil,
        "valide": bool(taux >= seuil),
        "categories_inconnues": valeurs[~valeurs_valides].unique().tolist(),
    }


def calculer_distribution(df, colonne):
    """Calcule le nombre et le pourcentage de chaque valeur d'une colonne."""
    distribution = (
        df[colonne]
        .fillna("NAN")
        .value_counts(dropna=False)
        .rename_axis("valeur")
        .reset_index(name="nombre")
    )
    distribution["pourcentage"] = (
        distribution["nombre"] / len(df) * 100 if len(df) else 0.0
    )
    return distribution




if __name__ == "__main__":
    # Exemple : remplacez ces données par pd.read_csv("votre_fichier.csv").
    reference = pd.DataFrame({
        "nom_ecole": ["Paris Descartes", "Paris Diderot", "HEC Paris", "Paris 6"],
        "typologie": ["universite", "universite", "ecole_commerce", "universite"],
        "C": ["REF200", "REF200", "AUTRE", "REF200"],
    })


    categories = {"universite", "ecole_commerce", "ecole_ingenieur", "institut"}

    print(verifier_non_nan(reference, "nom_ecole"))
    print(verifier_longueur(reference, "nom_ecole"))
    print(verifier_valeur_ref200(reference))
    print(verifier_categories(reference, "typologie", categories))
    print(calculer_distribution(reference, "typologie"))
