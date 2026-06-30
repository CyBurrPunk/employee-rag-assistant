from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import create_embeddings

documents = load_documents()

chunks = split_documents(documents)

texts, embeddings = create_embeddings(chunks)

print()

print("Number of Chunks")

print(len(texts))

print()

print("Embedding Dimension")

print(len(embeddings[0]))

print()

print("First Chunk")

print(texts[0])

print()

print("First Embedding")

print(embeddings[0][:10])