import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

docs = [
    "Python is a programming language.",
    "Dogs are common pets.",
    "RAG retrieves context for an LLM.",
]

model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = model.encode(docs, normalize_embeddings=True).astype("float32")

index = faiss.IndexFlatIP(vectors.shape[1])
index.add(vectors)

query = model.encode(["How does RAG retrieve information?"], normalize_embeddings=True).astype("float32")
scores, ids = index.search(query, 2)

for score, idx in zip(scores[0], ids[0]):
    print(round(float(score), 3), "->", docs[idx])
