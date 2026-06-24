# test/test_retriever.py
import json

from app.rag.retriever import retrieve_docs


results = retrieve_docs(
    "How often are creator payouts processed?"
)

with open(
    "test/retriever_output.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        indent=4,
        ensure_ascii=False
    )

print(
    "Results saved to test/retriever_output.json"
)