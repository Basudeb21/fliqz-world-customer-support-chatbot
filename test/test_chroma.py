# test/test_chroma.py
from app.db.chroma import get_collection


collection = get_collection()

print(
    "Total Documents:",
    collection.count()
)