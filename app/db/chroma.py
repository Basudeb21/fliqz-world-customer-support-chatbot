# app/db/chroma.py

import chromadb

from app.core.config import settings


client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_PATH
)


def get_collection():

    return client.get_or_create_collection(
        name=settings.CHROMA_COLLECTION,
        metadata={
            "description": "Fliqz World Support Knowledge Base"
        }
    )