import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

model_name = "bert-base-uncased"
# model_name = "camembert-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)
model.eval()

def splade_encode(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits  # [1, seq_len, vocab_size]

    # SPLADE pooling
    sparse_vec = torch.log1p(torch.relu(logits))

    # max pooling over tokens
    sparse_vec = torch.max(sparse_vec, dim=1).values  # [1, vocab_size]

    return sparse_vec.squeeze(0)


docs = [
    "BERT est un modèle transformer.",
    "SPLADE permet la recherche sparse.",
    "CamemBERT est adapté au français."
]

query = "recherche sémantique avec BERT"

doc_vecs = torch.stack([splade_encode(doc) for doc in docs])
query_vec = splade_encode(query)

scores = torch.matmul(doc_vecs, query_vec)

for score, doc in sorted(zip(scores, docs), reverse=True):
    print(float(score), doc)

vec = splade_encode("CamemBERT est utile pour la recherche documentaire")

topk = torch.topk(vec, k=20)

vocab = tokenizer.get_vocab()
id_to_token = {v: k for k, v in vocab.items()}

for idx, val in zip(topk.indices, topk.values):
    print(id_to_token[int(idx)], float(val))
