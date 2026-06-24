# test/test_chat.py
from app.llm.response_generator import generate_reply


question = "Can I save my filter settings?"

response = generate_reply(
    question
)

print(response)