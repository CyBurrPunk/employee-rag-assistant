from src.llm_service import generate_answer

prompt = """
Explain what Retrieval Augmented Generation is in simple language.
"""

answer = generate_answer(prompt)

print(answer)