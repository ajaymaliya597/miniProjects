from sentence_transformers import SentenceTransformer, CrossEncoder, util

docs = [
    "Python is used for data science.",
    "Python is a snake found in Asia.",
    "RAG retrieves documents before generation.",
    "Machine learning models learn patterns from data."
]

query = "How is Python used in data science?"

bi = SentenceTransformer("all-MiniLM-L6-v2")
q = bi.encode(query, convert_to_tensor=True)
d = bi.encode(docs, convert_to_tensor=True)

scores = util.cos_sim(q, d)[0]
top_ids = scores.argsort(descending=True)[:3].tolist()

cross = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
pairs = [[query, docs[i]] for i in top_ids]
rerank_scores = cross.predict(pairs)

for score, i in sorted(zip(rerank_scores, top_ids), reverse=True):
    print(round(float(score), 3), "->", docs[i])
