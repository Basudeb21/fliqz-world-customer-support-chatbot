# app/rag/retriever.py

from app.db.chroma import get_collection
from app.llm.embeddings import create_embedding

from app.core.config import settings


def retrieve_docs(query: str):

    collection = get_collection()

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=settings.RAG_TOP_K
    )

    return results


def retrieve_context(query: str):

    results = retrieve_docs(query)

    documents = results["documents"][0]
    distances = results["distances"][0]

    context_docs = []

    for doc, distance in zip(
        documents,
        distances
    ):

        if distance <= settings.RAG_SCORE_THRESHOLD:

            context_docs.append(doc)

    return "\n\n".join(context_docs)