from sentence_transformers import SentenceTransformer
import torch



from sentence_transformers import SentenceTransformer
import torch

model = SentenceTransformer("BAAI/bge-m3")

docs = [
    "Le machine learning permet de construire des modèles prédictifs.",
    "universite paris 5",
    "universite paris 6: descartes"
]

query = "Paris 5"

doc_emb = model.encode(
    docs,
    convert_to_tensor=True,
    normalize_embeddings=True
)

query_emb = model.encode(
    query,
    convert_to_tensor=True,
    normalize_embeddings=True
)

scores = query_emb @ doc_emb.T

print(scores)
print(docs[torch.argmax(scores)])
