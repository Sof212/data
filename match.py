import pandas as pd
import numpy as np
import re
from unidecode import unidecode
from rapidfuzz import fuzz
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def normalize(text):
    text = str(text).lower()
    text = unidecode(text)

    # enlever ponctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # mots inutiles
    stopwords = {
        "universite", "university", "univ",
        "ecole", "school", "college",
        "lycee", "institut"
    }

    tokens = text.split()
    tokens = [t for t in tokens if t not in stopwords]

    return " ".join(tokens)

df = pd.read_csv("data.csv")

# colonnes attendues :
# user_input | annotated_label

df["clean_input"] = df["user_input"].apply(normalize)
df["clean_label"] = df["annotated_label"].apply(normalize)


label_groups = (
    df.groupby("clean_label")["clean_input"]
    .apply(list)
    .to_dict()
)


model = SentenceTransformer("all-MiniLM-L6-v2")

# encoder tous les alias
all_aliases = df["clean_input"].tolist()
alias_embeddings = model.encode(all_aliases)

df["embedding"] = list(alias_embeddings)


label_centroids = {}

for label, group in df.groupby("clean_label"):
    embeddings = np.stack(group["embedding"].values)
    centroid = embeddings.mean(axis=0)
    
    label_centroids[label] = centroid


def get_top_k_labels(input_text, k=5):
    input_emb = model.encode([input_text])[0]
    
    scores = []
    
    for label, centroid in label_centroids.items():
        sim = cosine_similarity([input_emb], [centroid])[0][0]
        scores.append((label, sim))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    
    return [s[0] for s in scores[:k]]


def refine_with_aliases(input_text, candidates):
    best_label = None
    best_score = -1
    
    for label in candidates:
        aliases = label_groups[label]
        
        for alias in aliases:
            score = fuzz.token_sort_ratio(input_text, alias) / 100
            
            if score > best_score:
                best_score = score
                best_label = label
    
    return best_label, best_score

def predict(input_text):
    clean_text = normalize(input_text)
    
    # étape 1 : shortlist
    candidates = get_top_k_labels(clean_text, k=5)
    
    # étape 2 : matching fin
    label, score = refine_with_aliases(clean_text, candidates)
    
    return label, score

preds = []

for text in df["user_input"]:
    label, score = predict(text)
    preds.append((label, score))

df["predicted_label"] = [p[0] for p in preds]
df["score"] = [p[1] for p in preds]

def decision(score):
    if score > 0.85:
        return "auto_accept"
    elif score > 0.6:
        return "review"
    else:
        return "reject"

df["decision"] = df["score"].apply(decision)


def detect_bad_labels(threshold=0.5):
    bad = []
    
    for label, aliases in label_groups.items():
        if len(aliases) < 2:
            continue
        
        emb = model.encode(aliases)
        sim = cosine_similarity(emb)
        
        avg = sim.mean()
        
        if avg < threshold:
            bad.append((label, avg))
    
    return bad

bad_labels = detect_bad_labels()
print(bad_labels)




import re

def concat_word_number(text):
    """
    Concatène les mots suivis directement par un chiffre dans une chaîne de caractères.
    Exemple : "Paris 1" -> "Paris1"
    """
    if not isinstance(text, str):
        return ""
    
    # Remplacer "mot espace chiffre" par "motchiffre"
    text = re.sub(r'(\b\w+)\s+(\d+)\b', r'\1\2', text)
    return text.strip()

# Tests
examples = [
    "Paris 1",
    "Université Paris 1",
    "Paris",
    "Fac Lyon 2"
]

for e in examples:
    print(e, "->", concat_word_number(e))
