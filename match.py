import numpy as np
import torch
from rank_bm25 import BM25Okapi
from transformers import AutoTokenizer, AutoModel, AutoModelForSequenceClassification

# ─────────────────────────────────────────────
# CONFIG (download auto depuis Hugging Face)
# ─────────────────────────────────────────────

BI_ENCODER_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CROSS_ENCODER_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

DEVICE = "cpu"
torch.set_num_threads(4)

# ─────────────────────────────────────────────
# 1. BM25
# ─────────────────────────────────────────────

class BM25Retriever:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tokenized = [doc.lower().split() for doc in corpus]
        self.bm25 = BM25Okapi(self.tokenized)

    def search(self, query, top_k=20):
        scores = self.bm25.get_scores(query.lower().split())
        idx = np.argsort(scores)[::-1][:top_k]
        return [(self.corpus[i], scores[i]) for i in idx]


# ─────────────────────────────────────────────
# 2. BI-ENCODER
# ─────────────────────────────────────────────

class BiEncoder:
    def __init__(self, model_name):
        print(f"⏳ Loading bi-encoder: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(DEVICE)
        self.model.eval()

    def encode(self, texts):
        inputs = self.tokenizer(
            texts,
            padding=True,
            truncation=True,
            max_length=128,
            return_tensors="pt"
        ).to(DEVICE)

        with torch.no_grad():
            outputs = self.model(**inputs)

        embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings.cpu().numpy()


# ─────────────────────────────────────────────
# 3. CROSS-ENCODER
# ─────────────────────────────────────────────

class CrossEncoder:
    def __init__(self, model_name):
        print(f"⏳ Loading cross-encoder: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(DEVICE)
        self.model.eval()

    def score(self, query, docs):
        inputs = self.tokenizer(
            [query] * len(docs),
            docs,
            padding=True,
            truncation=True,
            max_length=128,
            return_tensors="pt"
        ).to(DEVICE)

        with torch.no_grad():
            logits = self.model(**inputs).logits

        return logits.squeeze().cpu().numpy()


# ─────────────────────────────────────────────
# 4. PIPELINE COMPLET
# ─────────────────────────────────────────────

class HybridSearch:
    def __init__(self, corpus):
        self.corpus = corpus

        print("🔹 BM25 init...")
        self.bm25 = BM25Retriever(corpus)

        print("🔹 Loading models...")
        self.bi = BiEncoder(BI_ENCODER_NAME)
        self.cross = CrossEncoder(CROSS_ENCODER_NAME)

        print("🔹 Encoding corpus...")
        self.doc_embeddings = self.bi.encode(corpus)

    def search(self, query, top_k=5):
        # 1. BM25
        bm25_results = self.bm25.search(query, top_k=30)
        docs = [d for d, _ in bm25_results]

        # 2. Bi-encoder
        q_emb = self.bi.encode([query])[0]
        doc_embs = self.bi.encode(docs)

        sims = np.dot(doc_embs, q_emb)
        top_idx = np.argsort(sims)[::-1][:15]
        docs = [docs[i] for i in top_idx]

        # 3. Cross-encoder
        scores = self.cross.score(query, docs)
        final_idx = np.argsort(scores)[::-1][:top_k]

        return [(docs[i], float(scores[i])) for i in final_idx]


