from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded successfully!")


def create_embeddings(chunks):

    texts = []

    for chunk in chunks:
        texts.append(chunk["content"])

    embeddings = model.encode(texts)

    return texts, embeddings