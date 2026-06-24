# app/llm/model.py
import requests

from app.core.config import settings


def generate(prompt: str):

    try:

        response = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]

    except Exception as e:

        print("Ollama Error:", e)

        return (
            "Sorry, I'm currently unable to process your request."
        )