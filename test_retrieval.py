from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import create_embeddings
from src.retriever import retrieve

documents = load_documents()

chunks = split_documents(documents)

texts, embeddings = create_embeddings(chunks)

query = "Can I carry forward annual leave?"

_, query_embedding = create_embeddings(
    [{"content": query}]
)

results = retrieve(
    query_embedding[0],
    embeddings,
    texts
)

print()

print("="*70)

print("TOP MATCHES")

print("="*70)

for i, result in enumerate(results):

    print()

    print(f"Result {i+1}")

    print(f"Similarity Score: {result['score']:.3f}")

    print()

    print(result["text"])

    print("-"*70)