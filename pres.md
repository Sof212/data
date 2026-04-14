# 🎓 Normalisation d'Entités : Résolution de Noms d'Écoles
### Modèle Hybride RapidFuzz × Cross-Encoder BERT

> **Contexte** : Réconciliation automatique de noms d'établissements saisis librement par des utilisateurs vers un référentiel canonique structuré.

---

## 📋 Plan

1. [Contexte & sources de données](#1--contexte--sources-de-données)
2. [Collecte & pré-traitement](#2--collecte--pré-traitement)
3. [Construction du dictionnaire d'aliases](#3--construction-du-dictionnaire-dalias)
4. [Architecture du modèle hybride](#4--architecture-du-modèle-hybride)
5. [Étage 1 — RapidFuzz (candidats)](#5--étage-1--rapidfuzz--candidats)
6. [Étage 2 — Cross-Encoder BERT (re-ranking)](#6--étage-2--cross-encoder-bert--re-ranking)
7. [Résultats & évaluation](#7--résultats--évaluation)

---

## 1 · Contexte & Sources de Données

### Problème posé

Un utilisateur saisit librement le nom de son école. Ce nom peut contenir :
- des **fautes de frappe** (`polytechniqe` au lieu de `polytechnique`)
- des **variantes historiques** (`Paris 5 Descartes` → `Université Paris Cité`)
- des **abréviations** (`UPMC`, `ENS Ulm`, `Sciences Po`)
- des **noms partiels** (`dauphine`, `centrale`)

**Objectif** : mapper toute saisie vers le **nom canonique officiel** de l'établissement.

---

### Les 5 sources de données

| # | Source | Type de saisie | Volume estimé |
|---|--------|---------------|--------------|
| A | CRM inscriptions | Formulaire libre | ~12 000 paires |
| B | Formulaires web | Autocomplete partiel | ~9 500 paires |
| C | Import CSV historique | Export brut legacy | ~8 000 paires |
| D | API partenaire | Données tierces | ~7 000 paires |
| E | Saisie back-office | Manuelle opérateurs | ~8 500 paires |

**Total : ~45 000 paires annotées** couvrant ~3 200 établissements distincts.

---

### Structure des datasets

Chaque source est un tableau à **2 colonnes** :

```
┌─────────────────────────────────────┬──────────────────────────────┐
│  nom_brut (saisi utilisateur)       │  nom_annote (label métier)   │
├─────────────────────────────────────┼──────────────────────────────┤
│  universite paris cité              │  Université Paris Cité       │
│  paris 5 descartes                  │  Université Paris Cité       │
│  upmc pierre et marie curie         │  Sorbonne Université         │
│  polytechniqe palaiseau  ← faute    │  École Polytechnique         │
│  sciences po paris                  │  Sciences Po                 │
│  ens ulm                            │  École Normale Supérieure    │
└─────────────────────────────────────┴──────────────────────────────┘
```

> 💡 **Observation clé** : la même école peut avoir en moyenne **8,3 aliases** différents à travers les 5 sources.

---

## 2 · Collecte & Pré-traitement

### Pipeline de nettoyage

```
[Source A]  [Source B]  [Source C]  [Source D]  [Source E]
    │           │           │           │           │
    └───────────┴───────────┴───────────┴───────────┘
                            │
                    ┌───────▼────────┐
                    │   FUSION       │
                    │  DataFrame     │
                    │  unifié        │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  NORMALISATION │
                    │  • lowercase   │
                    │  • strip accents│
                    │  • ponctuation │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  DÉBRUITAGE    │
                    │  • doublons    │
                    │  • vides/nulls │
                    │                │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  MAUVAISES     │
                    │  ANNOTATIONS   │
                    │                │
                    │                │
                    │                │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  DICTIONNAIRE  │
                    │  D'ALIASES     │
                    └────────────────┘
```

---


---




---


---

### Exemple de dictionnaire

```python
{
  "Université Paris Cité": [
      "universite paris cite",          # ← forme canonique normalisée
      "universite paris 5",
      "universite paris descartes",
      "paris 5",
      "paris descartes",
      "paris v",
      "upd",
      "universite rene descartes",
      "fac paris cite"
  ],

  "École Polytechnique": [
      "ecole polytechnique",
      "polytechnique",
      "polytechniqe palaiseau",          # ← faute de frappe conservée !
      "l x",
      "x palaiseau",
      "ecole polytechnique de palaiseau"
  ],

  "Sorbonne Université": [
      "sorbonne universite",
      "upmc",
      "pierre et marie curie",
      "universite pierre marie curie",
      "paris 6",
      "paris vi",
      "sorbonne paris 6"
  ],

  "HEC Paris": [
      "hec paris",
      "hec",
      "ecole des hautes etudes commerciales",
      "hautes etudes commerciales",
      "hec jouy en josas"
  ]
}
```

---

### Visualisation : cluster d'aliases

Chaque nœud central représente un **nom canonique**. Les nœuds satellites sont ses **aliases** détectés dans le corpus.

```
                    ┌─────────────────────────┐
                    │   Université Paris Cité  │  ← NOM CANONIQUE (clé)
                    └──────────┬──────────────┘
         ┌──────────┬──────────┼────────────┬──────────┐
         ▼          ▼          ▼            ▼          ▼
   "paris 5"  "descartes"  "paris v"   "upd"   "paris cite"
                                                  ...+4

                    ┌─────────────────────────┐
                    │    École Polytechnique   │  ← NOM CANONIQUE (clé)
                    └──────────┬──────────────┘
         ┌──────────┬──────────┼────────────┐
         ▼          ▼          ▼            ▼
   "l'X"  "polytechnique"  "x palaiseau"  "polytechniqe"  ← faute conservée
```

---



---

## 4 · Architecture du Modèle Hybride

### Vue d'ensemble

```
              INPUT : "universite paris cite" (saisie brute)
                                │
                    ┌───────────▼───────────┐
                    │   NORMALISATION       │
                    │   normalize(input)    │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼───────────┐
                    │      ÉTAGE 1          │
                    │   RapidFuzz           │
                    │   (fuzzy matching)    │
                    │                       │
                    │  Compare input vs     │
                    │  TOUS les aliases     │
                    │  du dictionnaire      │
                    │                       │
                    │  → Top-15 candidats   │
                    └───────────┬───────────┘
                                │ 15 candidats + scores
                    ┌───────────▼───────────┐
                    │      ÉTAGE 2          │
                    │  Cross-Encoder BERT   │
                    │  (re-ranking)         │
                    │                       │
                    │  Score sémantique     │
                    │  (input, candidat_i)  │
                    │  pour i ∈ [1..15]     │
                    │                       │
                    │  → Meilleur score     │
                    └───────────┬───────────┘
                                │
              OUTPUT : "Université Paris Cité" ✓
```

---

### Pourquoi un modèle hybride ?

| Critère | Fuzzy seul | BERT seul | **Hybride** |
|---------|-----------|----------|------------|
| Vitesse |  Très rapide |  Lent sur tout le corpus |  Rapide |
| Robustesse aux fautes |  Excellent |  Moyen |  Excellent |
| Compréhension sémantique |  Aucune |  Excellente |  Excellente |
| Scalabilité |  O(n) linéaire |  O(n) × inference |  O(15) BERT calls |
|

> **Idée clé** : RapidFuzz est un filtre rapide qui garantit que la bonne réponse est dans le Top-15. BERT choisit ensuite le meilleur parmi ces 15 candidats.

---

## 5 · Étage 1 — RapidFuzz (Candidats)

### Principe du fuzzy matching

RapidFuzz calcule plusieurs métriques de **distance d'édition** entre chaînes de caractères.

**Distance de Levenshtein normalisée :**

$$d_{edit}(s_1, s_2) = 1 - \frac{\text{Levenshtein}(s_1, s_2)}{\max(|s_1|, |s_2|)}$$

**Token Sort Ratio** (robustesse à l'ordre des mots) :

$$\text{TSR}(s_1, s_2) = \text{ratio}\left(\text{sort\_tokens}(s_1),\ \text{sort\_tokens}(s_2)\right)$$

**Weighted Ratio** (combinaison de plusieurs métriques) :

$$\text{WR}(s_1, s_2) = \max\left(\text{ratio}, \text{partial\_ratio}, \text{TSR}, \text{TSeR}\right)$$

---

### Exemple de sortie — Top-15 candidats

Input : `"universite paris cite"`

```
Rang  Alias matché               Score RF   École canonique
─────────────────────────────────────────────────────────────
  1   universite paris cite        98.5    Université Paris Cité   ← ✓
  2   universite paris cite        95.2    Université Paris 1
  3   universite paris cite        93.8    Université Paris 8
  4   universite paris 5           91.4    Université Paris Cité
  5   universite de paris          89.6    Université de Paris
  ...
 15   paris sciences lettres       72.1    PSL Research University
```


---

## 6 · Étage 2 — Cross-Encoder BERT (Re-ranking)

### Principe du Cross-Encoder

Contrairement à un Bi-Encoder (où query et document sont encodés séparément), le **Cross-Encoder** concatène les deux chaînes et calcule un score de similarité conjoint :

$$\text{score}(q, d) = \text{CrossEncoder}\left([CLS]\ q\ [SEP]\ d\ [SEP]\right)$$

Ce score capture les **interactions sémantiques fines** entre l'input et chaque candidat.

---

### Architecture du Cross-Encoder BERT

```
Input :  "universite paris cite"  +  "Université Paris Cité"
          ↓                              ↓
         [CLS]  u n i v e r s i t e ... [SEP] U n i v e r s i t é ... [SEP]
          │
          ▼
   ┌──────────────────────────────────────────────────┐
   │              BERT Encoder (12 couches)            │
   │                                                  │
   │   Layer 1 :  Self-Attention + FFN                │
   │   Layer 2 :  Self-Attention + FFN                │
   │      ...                                         │
   │   Layer 12:  Self-Attention + FFN                │
   └──────────────────────┬───────────────────────────┘
                          │  hidden_state [CLS]  (768-dim)
                          ▼
                  ┌───────────────┐
                  │  Linear Layer │  (768 → 1)
                  └───────┬───────┘
                          │
                  score ∈ [0, 1]   ← similarité sémantique
```

---

### Exemple de re-ranking

Input : `"universite paris cite"`

```
Rang RF  École canonique               Score RF   Score BERT   Rang BERT
──────────────────────────────────────────────────────────────────────────
   1     Université Paris Cité           98.5       0.934         1  ✓
   2     Université Paris 1              95.2       0.421         6
   3     Université Paris 8              93.8       0.398         7
   4     Université Paris Cité           91.4       —            (déjà vu)
   5     Université de Paris             89.6       0.687         2
   ...
```

> Le Cross-Encoder confirme le rang 1 de RapidFuzz **et** corrige les cas où RapidFuzz se trompe (ex. noms courts ou très ambigus).

---

### Score final combiné (optionnel)

On peut aussi construire un score hybride pondéré :

$$\text{score\_final}(q, d) = \alpha \cdot \frac{\text{score\_RF}}{100} + (1 - \alpha) \cdot \text{score\_BERT}$$

avec $\alpha \in [0, 1]$ calibré sur le jeu de validation. En pratique, $\alpha = 0$ (BERT seul) sur le Top-15 donne les meilleurs résultats.

---
