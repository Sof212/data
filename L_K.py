import numpy as np
from sentence_transformers import SentenceTransformer, util

# =========================
# 🔥 MODEL
# =========================

model = SentenceTransformer("sentence-transformers/LaBSE")

# =========================
# 🔥 NORMALISATION
# =========================

def normalize(text):
    return text.lower().strip()

# =========================
# 🔥 EMBEDDING
# =========================

def encode(texts):
    return model.encode(texts)

# =========================
# 🔥 SIMILARITY
# =========================

def similarity(a, b):
    return util.cos_sim(a, b).item()

# =========================
# 🔥 CENTROID
# =========================

def compute_centroid(aliases):
    emb = encode(aliases)
    return np.mean(emb, axis=0)

# =========================
# 🔥 PIPELINE CLEAN
# =========================

def clean_dictionary(data, threshold_in=0.55, margin=0.05):
    
    """
    threshold_in : minimum similarity avec son cluster
    margin : différence minimale avec les autres clusters
    """
    
    # 🔥 préparation
    clusters = {}
    
    for k, values in data.items():
        clusters[k] = [normalize(v) for v in values]
    
    # 🔥 centroids
    centroids = {}
    
    for k, aliases in clusters.items():
        if len(aliases) > 0:
            centroids[k] = compute_centroid(aliases)
    
    result = {}
    
    for key, aliases in clusters.items():
        
        cleaned = []
        
        for alias in aliases:
            
            emb = model.encode([alias])[0]
            
            # 🔥 similarité avec son cluster
            own_centroid = centroids.get(key)
            
            if own_centroid is None:
                continue
            
            sim_own = similarity([emb], [own_centroid])
            
            # ❌ trop faible → suppression
            if sim_own < threshold_in:
                continue
            
            # 🔥 comparaison avec autres clusters
            better_cluster = False
            
            for other_key, other_centroid in centroids.items():
                
                if other_key == key:
                    continue
                
                sim_other = similarity([emb], [other_centroid])
                
                if sim_other > sim_own + margin:
                    better_cluster = True
                    break
            
            # ❌ appartient clairement à un autre cluster
            if better_cluster:
                continue
            
            cleaned.append(alias)
        
        result[key] = cleaned
    
    return result

# =========================
# 🔥 EXEMPLE
# =========================

if __name__ == "__main__":
    
    data = {
        "hec_paris": [
            "hec",
            "haut etudes commerciales"
        ],
        "ecole_polytechnique": [
            "x",
            "l'x",
            "polytechnique",
            "ecole_polytechnique",
            "paris cite"  # ❌ doit être supprimé
        ],
        "universite paris cite": [
            "universite paris cite",
            "paris descartes",
            "es banque"
        ],
    "es banque": [
            "es banque Paris",

        ],
  
    }

    result = clean_dictionary(data)

    for key, values in result.items():
        print(f"\n📚 {key}")
        for v in values:
            print("  -", v)
