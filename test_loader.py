from src.pdf_loader import load_documents

documents = load_documents()

for doc in documents:

    print("=" * 50)

    print(doc["file_name"])

    print(doc["content"][:500])

    print()