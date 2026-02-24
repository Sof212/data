# ------------------------
# 1️⃣ Importations
# ------------------------
from sentence_transformers import SentenceTransformer, CrossEncoder, InputExample, losses
from torch.utils.data import DataLoader
from rapidfuzz import process
import numpy as np
import unicodedata

# ------------------------
# 2️⃣ Nettoyage du texte
# ------------------------
def clean_text(text):
    text = text.lower().strip()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    text = text.replace("-", " ").replace("’", "'")
    return text

# ------------------------
# 3️⃣ Référentiel canonique
# ------------------------
referentiel = [
    "HEC Paris",
    "Sorbonne Paris Nord",
    "École Polytechnique",
    "Université Paris Dauphine",
    "Paris Panthéon Assas",
    "Université Paris-Saclay"
]

# ------------------------
# 4️⃣ Aliases
# ------------------------
CANONICAL_TO_ALIASES = {
    "HEC Paris": ["hec", "hec paris", "hec business school", "hautes etudes commerciales"],
    "Sorbonne Paris Nord": ["paris 13", "paris xiii", "universite paris 13", "paris nord"],
    "École Polytechnique": ["x", "l'x", "polytechnique", "ecole polytechnique", "ecole d'ingénieur x"],
    "Université Paris Dauphine": ["dauphine", "paris dauphine", "universite dauphine", "dauphine psl"],
    "Paris Panthéon Assas": ["assas", "pantheon assas", "universite assas", "paris assas"],
    "Université Paris-Saclay": ["paris saclay", "universite paris saclay", "u-psl"]
}

ALIAS_TO_CANONICAL = {}
for canonical, aliases in CANONICAL_TO_ALIASES.items():
    for alias in aliases:
        ALIAS_TO_CANONICAL[clean_text(alias)] = canonical
for canonical in referentiel:
    ALIAS_TO_CANONICAL[clean_text(canonical)] = canonical

# ------------------------
# 5️⃣ Charger les modèles
# ------------------------
bi_encoder = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

# Embeddings BiEncoder pour le référentiel
ref_embeddings = bi_encoder.encode(referentiel, normalize_embeddings=True)

# ------------------------
# 6️⃣ Fonction Sigmoid pour CrossEncoder
# ------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ------------------------
# 7️⃣ Fonction normalize
# ------------------------
def normalize(name, fuzzy_threshold=0.85, ai_threshold=0.9):
    name_clean = clean_text(name)

    # 1️⃣ Alias exact
    if name_clean in ALIAS_TO_CANONICAL:
        return {"input": name, "canonical": ALIAS_TO_CANONICAL[name_clean], "score": 1.0, "method": "alias"}

    # 2️⃣ Fuzzy matching
    candidates_aliases = list(ALIAS_TO_CANONICAL.keys())
    best_match, score, _ = process.extractOne(name_clean, candidates_aliases)
    normalized_score = score / 100

    if normalized_score >= ai_threshold:
        return {"input": name, "canonical": ALIAS_TO_CANONICAL[best_match], "score": normalized_score, "method": "fuzzy"}

    # 3️⃣ IA BiEncoder + CrossEncoder
    query_emb = bi_encoder.encode([name_clean], normalize_embeddings=True)
    scores = np.dot(query_emb, ref_embeddings.T)[0]
    top_idx = np.argsort(scores)[-5:]
    candidates = [referentiel[i] for i in top_idx]

    pairs = [[name, candidate] for candidate in candidates]
    ce_scores = cross_encoder.predict(pairs)
    best_idx = np.argmax(ce_scores)
    best = candidates[best_idx]
    confidence = sigmoid(ce_scores[best_idx])

    return {"input": name, "canonical": best, "score": float(confidence), "method": "ai"}

# ------------------------
# 8️⃣ Exemple de dataset pour fine-tuning CrossEncoder
# ------------------------
train_examples = [
    InputExample(texts=["ecole d'ingénieur X", "École Polytechnique"], label=1.0),
    InputExample(texts=["La prestigieuse école X", "École Polytechnique"], label=1.0),
    InputExample(texts=["juif", "École Polytechnique"], label=1.0),
    InputExample(texts=["l'école polytechnique", "École Polytechnique"], label=1.0),
    InputExample(texts=["Paris 13", "Sorbonne Paris Nord"], label=1.0),
    InputExample(texts=["dauphine", "Université Paris Dauphine"], label=1.0),
    InputExample(texts=["ecole d'ingénieur X", "Sorbonne Paris Nord"], label=0.0),
    InputExample(texts=["Paris 13", "École Polytechnique"], label=0.0),
]

train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=4)
train_loss = losses.CosineSimilarityLoss(cross_encoder)

# ------------------------
# 9️⃣ Fine-tuning (CrossEncoder)
# ------------------------
# Pour un vrai entraînement, utilisez model.fit avec un optimiseur et plusieurs epochs
# Exemple rapide pour montrer le pipeline
# cross_encoder.fit(train_dataloader=train_dataloader, epochs=2, warmup_steps=10)

# ------------------------
# 10️⃣ Tests
# ------------------------
tests = [
    "Paris 13",
    "l'X",
    "polytechnique",
    "HEC",
    "Dauphine",
    "Pantheon Assas",
    "université daufine",
    "univeresité pariss 13",
    "paris saclay",
    "ecole d'ingénieur X",
    "La prestigieuse école polytechnique"
]

for t in tests:
    print(normalize(t))
