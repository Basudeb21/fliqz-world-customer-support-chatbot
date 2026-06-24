# app/schemas/history.py
from pydantic import BaseModel
from datetime import datetime


class ChatHistoryResponse(BaseModel):

    id: int
    message: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True