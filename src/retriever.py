from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def retrieve(query_embedding, embeddings, texts, top_k=3):

    similarities = cosine_similarity(
        [query_embedding],
        embeddings
    )[0]

    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []

    for idx in top_indices:

        results.append(
            {
                "text": texts[idx],
                "score": similarities[idx]
            }
        )

    return results