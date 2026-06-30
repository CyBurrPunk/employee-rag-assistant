from src.chroma_store import search
from src.prompt_builder import build_prompt
from src.llm_service import generate_answer


def ask_question(collection, question):

    results = search(collection, question)

    retrieved_docs = results["documents"][0]

    prompt = build_prompt(
        question,
        retrieved_docs
    )

    answer = generate_answer(prompt)

    sources = []

    for metadata in results["metadatas"][0]:
        sources.append(metadata["source"])

    return answer, list(set(sources))