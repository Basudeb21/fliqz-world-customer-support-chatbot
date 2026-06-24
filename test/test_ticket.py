# test/test_ticket.py
from app.db.database import SessionLocal

from app.repositories.ticket_repository import (
    TicketRepository
)


db = SessionLocal()

repo = TicketRepository(db)

ticket = repo.create_ticket(
    ticket_number="FLQ-0001",
    user_id=1,
    ticket_type="Other",
    complaint_message="This is a test ticket"
)

print(ticket.id)
print(ticket.ticket_number)

db.close()