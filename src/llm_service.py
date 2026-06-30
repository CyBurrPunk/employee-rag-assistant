from google import genai
from src.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_answer(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text