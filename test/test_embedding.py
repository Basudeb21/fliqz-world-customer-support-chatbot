# test/test_embedding.py
from app.llm.embeddings import create_embedding


embedding = create_embedding(
    "How do I access advanced filters?"
)
          
print(type(embedding))
print(len(embedding))
print(embedding[:5])