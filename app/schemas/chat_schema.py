# app/schemas/chat_schema.py
from pydantic import BaseModel


class ChatRequest(BaseModel):

    user_id: int
    message: str


class ChatResponse(BaseModel):

    type: str
    response: str