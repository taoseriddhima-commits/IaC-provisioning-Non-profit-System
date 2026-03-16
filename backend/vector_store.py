import chromadb
from chromadb.utils import embedding_functions

# --------------------------------------------------
# Persistent Chroma Client (saves to disk)
# --------------------------------------------------
client = chromadb.PersistentClient(path="./chroma_db")

# --------------------------------------------------
# Embedding Model
# --------------------------------------------------
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# --------------------------------------------------
# Collection (Created Once, Reused Automatically)
# --------------------------------------------------
collection = client.get_or_create_collection(
    name="triage_history",
    embedding_function=embedding_function
)

# --------------------------------------------------
# Save Case to Vector Database
# --------------------------------------------------
def save_case(case_id: str, message: str, metadata: dict):
    """
    Stores a processed case into the vector database.

    Args:
        case_id (str): Unique identifier (use uuid)
        message (str): Original user message
        metadata (dict): Classification + response info
    """
    collection.add(
        documents=[message],
        metadatas=[metadata],
        ids=[case_id]
    )


# --------------------------------------------------
# Retrieve All Stored Cases
# --------------------------------------------------
def get_all_cases():
    """
    Returns all stored cases from the collection.
    """
    return collection.get()


# --------------------------------------------------
# Semantic Search (Optional – For Later Use)
# --------------------------------------------------
def search_similar_cases(query_text: str, n_results: int = 3):
    """
    Searches for semantically similar past cases.
    """
    return collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
