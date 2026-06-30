import chromadb
from chromadb.utils import embedding_functions

# Create persistent client
client = chromadb.PersistentClient(path="db")

# Embedding model
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

COLLECTION_NAME = "employee_docs"


def index_chunks(chunks):
    """
    Creates a fresh Chroma collection and indexes all document chunks.
    """

    # Delete old collection if it exists
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    # Create new collection
    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    ids = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(str(i))
        documents.append(chunk["content"])
        metadatas.append(
            {
                "source": chunk["source"]
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

    print(f"Indexed {len(ids)} chunks successfully!")

    return collection


def search(collection, query, top_k=3):
    """
    Search the vector database.
    """

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results