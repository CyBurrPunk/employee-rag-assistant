from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.chroma_store import index_chunks, search

# Load documents
documents = load_documents()

# Split into chunks
chunks = split_documents(documents)

# Index in ChromaDB
collection = index_chunks(chunks)

# Ask a question
query = "Can I carry forward annual leave?"

results = search(collection, query)

print("\nTop Results:\n")

for i in range(len(results["documents"][0])):
    print(f"Result {i+1}")
    print(f"Source: {results['metadatas'][0][i]['source']}")
    print(f"Document:\n{results['documents'][0][i]}")
    print("-" * 80)