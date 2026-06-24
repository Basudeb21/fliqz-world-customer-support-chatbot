# test/test_reply.py
from app.llm.response_generator import generate_reply


context = """
Users can upload videos from the Upload page.
Supported formats are mp4 and mov.
Maximum upload size is 500MB.
"""

question = "How do I upload a video?"


response = generate_reply(
    context=context,
    question=question
)

print(response)