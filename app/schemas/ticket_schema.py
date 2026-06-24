# app/schemas/ticket_schema.py
from pydantic import BaseModel
from datetime import datetime


class TicketResponse(BaseModel):

    id: int
    ticket_number: str
    ticket_type: str
    complaint_message: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True