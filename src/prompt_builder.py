def build_prompt(question, retrieved_docs):

    context = "\n\n".join(retrieved_docs)

    prompt = f"""
You are an HR assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, say:
"I couldn't find this information in the available documents."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt