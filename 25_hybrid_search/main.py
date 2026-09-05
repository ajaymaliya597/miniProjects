from sentence_transformers import SentenceTransformer, util

docs = [
    "Python programming language tutorial",
    "Machine learning with Python",
    "Java backend development",
]

query = "Python machine learning"

# Keyword score
q_words = set(query.lower().split())
keyword = []
for d in docs:
    words = set(d.lower().split())
    keyword.append(len(q_words & words))

# Semantic score
model = SentenceTransformer("all-MiniLM-L6-v2")
q = model.encode(query, convert_to_tensor=True)
emb = model.encode(docs, convert_to_tensor=True)
semantic = util.cos_sim(q, emb)[0].tolist()

# Simple hybrid score
final = [k + float(s) for k, s in zip(keyword, semantic)]

for score, doc in sorted(zip(final, docs), reverse=True):
    print(round(score, 3), "->", doc)
