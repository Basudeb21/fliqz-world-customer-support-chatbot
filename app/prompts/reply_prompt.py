# app/prompts/reply_prompt.py
from app.constants.contacts import (
    SUPPORT_EMAIL,
    SUPPORT_CALL
)

from app.prompts.system_prompt import (
    build_system_prompt
)


def build_prompt(
    context: str,
    history: str,
    question: str
):

    return f"""
{build_system_prompt()}

Support Contact:
Email: {SUPPORT_EMAIL}
Phone: {SUPPORT_CALL}

Conversation History:
{history}

Knowledge Base:
{context}

Current User Question:
{question}

Answer:
"""