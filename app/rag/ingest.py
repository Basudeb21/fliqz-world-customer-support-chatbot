# app/rag/ingest.py
import json

from app.db.chroma import get_collection
from app.llm.embeddings import create_embedding


def load_faq_data():

    with open(
        "data/support_docs.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def ingest():

    collection = get_collection()

    faqs = load_faq_data()

    documents = []
    embeddings = []
    ids = []
    metadatas = []

    for faq in faqs:

        document = (
            f"Question: {faq['label']}\n\n"
            f"Answer: {faq['answer']}"
        )

        embedding = create_embedding(
            document
        )

        documents.append(document)

        embeddings.append(embedding)

        ids.append(
            str(faq["id"])
        )

        metadatas.append(
            {
                "faq_id": faq["id"],
                "question": faq["label"],
                "url": faq["url"]
            }
        )

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(
        f"Successfully ingested {len(faqs)} FAQs."
    )


if __name__ == "__main__":
    ingest()