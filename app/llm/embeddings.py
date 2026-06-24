# app/llm/embeddings.py

import requests

from app.core.config import settings


def create_embedding(text: str):

    response = requests.post(
        f"{settings.OLLAMA_BASE_URL}/api/embed",
        json={
            "model": settings.OLLAMA_EMBED_MODEL,
            "input": text
        },
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    return data["embeddings"][0]