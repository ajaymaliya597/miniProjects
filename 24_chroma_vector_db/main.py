import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="notes",
    embedding_function=embedding_fn
)

collection.upsert(
    ids=["1", "2", "3"],
    documents=[
        "Python is a programming language.",
        "RAG retrieves relevant context.",
        "Kafka transports streaming events."
    ]
)

result = collection.query(
    query_texts=["How do I retrieve context for an LLM?"],
    n_results=2
)

print(result["documents"])
