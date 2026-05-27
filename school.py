import pandas as pd
import matplotlib.pyplot as plt
from rapidfuzz import fuzz
import os

# =========================
# CONFIGURATION
# =========================

INPUT_FILE = "dataset.csv"
OUTPUT_DIR = "resultats_analyse_ecoles"

RAW_COL = "raw_school_name"
SOURCE_COL = "source_flag"
NORMALIZED_COL = "normalized_name"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# CHARGEMENT
# =========================

df = pd.read_csv(INPUT_FILE)

# Si ton fichier n'a pas les bons noms de colonnes
df.columns = [RAW_COL, SOURCE_COL, NORMALIZED_COL]

df[RAW_COL] = df[RAW_COL].astype(str).str.strip()
df[NORMALIZED_COL] = df[NORMALIZED_COL].astype(str).str.strip()

df["referentiel"] = df[SOURCE_COL].map({
    1: "A",
    0: "B"
})

# =========================
# 1. ANALYSE GLOBALE A / B
# =========================

global_stats = df["referentiel"].value_counts().reset_index()
global_stats.columns = ["referentiel", "nombre_lignes"]
global_stats["pourcentage"] = global_stats["nombre_lignes"] / len(df) * 100

print("\n=== Répartition A / B ===")
print(global_stats)

global_stats.to_csv(
    f"{OUTPUT_DIR}/repartition_A_B.csv",
    index=False
)

# =========================
# 2. TOP 10 ECOLES REDONDANTES PAR REFERENTIEL
# =========================

top_redundant = (
    df.groupby(["referentiel", NORMALIZED_COL])
    .size()
    .reset_index(name="occurrences")
    .sort_values(["referentiel", "occurrences"], ascending=[True, False])
)

top_10_by_ref = (
    top_redundant
    .groupby("referentiel")
    .head(10)
)

print("\n=== Top 10 écoles redondantes par référentiel ===")
print(top_10_by_ref)

top_10_by_ref.to_csv(
    f"{OUTPUT_DIR}/top_10_ecoles_redondantes_A_B.csv",
    index=False
)

# =========================
# 3. POUR CHAQUE TOP ECOLE : TOUS LES NOMS BRUTS
# =========================

raw_names_top = []

for _, row in top_10_by_ref.iterrows():
    ref = row["referentiel"]
    school = row[NORMALIZED_COL]

    subset = df[
        (df["referentiel"] == ref) &
        (df[NORMALIZED_COL] == school)
    ]

    raw_names = subset[RAW_COL].value_counts()

    for raw_name, count in raw_names.items():
        raw_names_top.append({
            "referentiel": ref,
            "ecole_normalisee": school,
            "nom_brut": raw_name,
            "occurrences_nom_brut": count
        })

raw_names_top_df = pd.DataFrame(raw_names_top)

print("\n=== Noms bruts pour les écoles les plus redondantes ===")
print(raw_names_top_df)

raw_names_top_df.to_csv(
    f"{OUTPUT_DIR}/noms_bruts_top_10_ecoles.csv",
    index=False
)

# =========================
# 4. ECOLES AVEC LE PLUS DE VARIANTES
# =========================

variants = (
    df.groupby(NORMALIZED_COL)[RAW_COL]
    .nunique()
    .reset_index(name="nombre_variantes_brutes")
    .sort_values("nombre_variantes_brutes", ascending=False)
)

print("\n=== Écoles avec le plus de variantes ===")
print(variants.head(20))

variants.to_csv(
    f"{OUTPUT_DIR}/ecoles_avec_plus_de_variantes.csv",
    index=False
)

# =========================
# 5. TAUX DE NORMALISATION / COMPRESSION
# =========================

unique_raw = df[RAW_COL].nunique()
unique_normalized = df[NORMALIZED_COL].nunique()

normalization_stats = pd.DataFrame([{
    "nombre_lignes": len(df),
    "noms_bruts_uniques": unique_raw,
    "noms_normalises_uniques": unique_normalized,
    "ratio_compression": unique_normalized / unique_raw
}])

print("\n=== Statistiques de normalisation ===")
print(normalization_stats)

normalization_stats.to_csv(
    f"{OUTPUT_DIR}/statistiques_normalisation.csv",
    index=False
)

# =========================
# 6. ECOLES COMMUNES ENTRE A ET B
# =========================

schools_A = set(df[df["referentiel"] == "A"][NORMALIZED_COL])
schools_B = set(df[df["referentiel"] == "B"][NORMALIZED_COL])

common_schools = schools_A.intersection(schools_B)
only_A = schools_A - schools_B
only_B = schools_B - schools_A

common_df = pd.DataFrame({"ecole_normalisee": list(common_schools)})
only_A_df = pd.DataFrame({"ecole_normalisee": list(only_A)})
only_B_df = pd.DataFrame({"ecole_normalisee": list(only_B)})

common_df.to_csv(f"{OUTPUT_DIR}/ecoles_communes_A_B.csv", index=False)
only_A_df.to_csv(f"{OUTPUT_DIR}/ecoles_uniquement_A.csv", index=False)
only_B_df.to_csv(f"{OUTPUT_DIR}/ecoles_uniquement_B.csv", index=False)

print("\n=== Écoles communes A/B ===")
print(len(common_schools))

print("Écoles uniquement A :", len(only_A))
print("Écoles uniquement B :", len(only_B))

# =========================
# 7. DETECTION DE NORMALISATIONS SUSPECTES
# =========================

df["similarity_score"] = df.apply(
    lambda row: fuzz.token_sort_ratio(
        row[RAW_COL],
        row[NORMALIZED_COL]
    ),
    axis=1
)

suspicious = df[df["similarity_score"] < 40].copy()

suspicious = suspicious.sort_values("similarity_score")

print("\n=== Normalisations suspectes ===")
print(suspicious[[RAW_COL, NORMALIZED_COL, "referentiel", "similarity_score"]].head(30))

suspicious.to_csv(
    f"{OUTPUT_DIR}/normalisations_suspectes.csv",
    index=False
)

# =========================
# 8. ECOLES AVEC BEAUCOUP DE VARIANTES SUSPECTES
# =========================

suspicious_by_school = (
    suspicious.groupby(NORMALIZED_COL)
    .size()
    .reset_index(name="nombre_cas_suspects")
    .sort_values("nombre_cas_suspects", ascending=False)
)

print("\n=== Écoles avec le plus de cas suspects ===")
print(suspicious_by_school.head(20))

suspicious_by_school.to_csv(
    f"{OUTPUT_DIR}/ecoles_avec_plus_de_cas_suspects.csv",
    index=False
)

# =========================
# 9. ANALYSE DES NOMS BRUTS QUI MAPPENT VERS PLUSIEURS ECOLES
# =========================

ambiguous_raw = (
    df.groupby(RAW_COL)[NORMALIZED_COL]
    .nunique()
    .reset_index(name="nombre_ecoles_normalisees")
)

ambiguous_raw = ambiguous_raw[
    ambiguous_raw["nombre_ecoles_normalisees"] > 1
].sort_values("nombre_ecoles_normalisees", ascending=False)

print("\n=== Noms bruts ambigus ===")
print(ambiguous_raw.head(20))

ambiguous_raw.to_csv(
    f"{OUTPUT_DIR}/noms_bruts_ambigus.csv",
    index=False
)

# Détail des noms bruts ambigus
ambiguous_details = df[
    df[RAW_COL].isin(ambiguous_raw[RAW_COL])
].sort_values(RAW_COL)

ambiguous_details.to_csv(
    f"{OUTPUT_DIR}/details_noms_bruts_ambigus.csv",
    index=False
)

# =========================
# 10. ANALYSE DES ACRONYMES
# =========================

def is_acronym(text):
    text = str(text).replace(".", "").replace(" ", "")
    return text.isupper() and len(text) <= 10

df["raw_is_acronym"] = df[RAW_COL].apply(is_acronym)
df["normalized_is_acronym"] = df[NORMALIZED_COL].apply(is_acronym)

acronyms = df[
    df["raw_is_acronym"] | df["normalized_is_acronym"]
]

print("\n=== Cas avec acronymes ===")
print(acronyms[[RAW_COL, NORMALIZED_COL, "referentiel"]].head(30))

acronyms.to_csv(
    f"{OUTPUT_DIR}/analyse_acronymes.csv",
    index=False
)

# =========================
# 11. SCORE MOYEN PAR REFERENTIEL
# =========================

score_by_ref = (
    df.groupby("referentiel")["similarity_score"]
    .agg(["mean", "median", "min", "max"])
    .reset_index()
)

print("\n=== Score moyen de similarité par référentiel ===")
print(score_by_ref)

score_by_ref.to_csv(
    f"{OUTPUT_DIR}/score_similarite_par_referentiel.csv",
    index=False
)

# =========================
# 12. GRAPHIQUES
# =========================

plt.figure(figsize=(6, 6))
plt.pie(
    global_stats["nombre_lignes"],
    labels=global_stats["referentiel"],
    autopct="%1.1f%%"
)
plt.title("Répartition des lignes par référentiel")
plt.savefig(f"{OUTPUT_DIR}/repartition_A_B.png")
plt.close()

for ref in ["A", "B"]:
    data = top_10_by_ref[top_10_by_ref["referentiel"] == ref]

    plt.figure(figsize=(12, 6))
    plt.bar(data[NORMALIZED_COL], data["occurrences"])
    plt.title(f"Top 10 écoles redondantes - Référentiel {ref}")
    plt.xlabel("École normalisée")
    plt.ylabel("Occurrences")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/top_10_ecoles_{ref}.png")
    plt.close()

plt.figure(figsize=(12, 6))
plt.hist(df["similarity_score"], bins=30)
plt.title("Distribution des scores de similarité")
plt.xlabel("Score de similarité")
plt.ylabel("Nombre de lignes")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/distribution_scores_similarite.png")
plt.close()

plt.figure(figsize=(12, 6))
plt.bar(
    variants.head(20)[NORMALIZED_COL],
    variants.head(20)["nombre_variantes_brutes"]
)
plt.title("Top 20 écoles avec le plus de variantes brutes")
plt.xlabel("École normalisée")
plt.ylabel("Nombre de variantes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/top_20_variantes.png")
plt.close()

# =========================
# 13. RAPPORT TEXTE
# =========================

with open(f"{OUTPUT_DIR}/rapport_analyse.txt", "w", encoding="utf-8") as f:
    f.write("RAPPORT D'ANALYSE DU DATASET ECOLES\n")
    f.write("=" * 50 + "\n\n")

    f.write(f"Nombre total de lignes : {len(df)}\n")
    f.write(f"Lignes référentiel A : {len(df[df['referentiel'] == 'A'])}\n")
    f.write(f"Lignes référentiel B : {len(df[df['referentiel'] == 'B'])}\n\n")

    f.write(f"Noms bruts uniques : {unique_raw}\n")
    f.write(f"Noms normalisés uniques : {unique_normalized}\n")
    f.write(f"Ratio de compression : {unique_normalized / unique_raw:.4f}\n\n")

    f.write(f"Écoles communes A/B : {len(common_schools)}\n")
    f.write(f"Écoles uniquement A : {len(only_A)}\n")
    f.write(f"Écoles uniquement B : {len(only_B)}\n\n")

    f.write("Top 10 écoles redondantes par référentiel :\n")
    f.write(top_10_by_ref.to_string(index=False))

    f.write("\n\nÉcoles avec le plus de variantes :\n")
    f.write(variants.head(20).to_string(index=False))

    f.write("\n\nNormalisations suspectes :\n")
    f.write(
        suspicious[
            [RAW_COL, NORMALIZED_COL, "referentiel", "similarity_score"]
        ].head(30).to_string(index=False)
    )

print("\nAnalyse terminée.")
print(f"Tous les résultats sont dans le dossier : {OUTPUT_DIR}")
