from src.pdf_loader import load_documents
from src.text_splitter import split_documents

documents = load_documents()

chunks = split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

print()

print(chunks[0]["content"])