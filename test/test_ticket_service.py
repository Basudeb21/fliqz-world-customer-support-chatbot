# test/test_ticket_service.py
from app.db.database import SessionLocal

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.services.ticket_service import (
    TicketService
)


db = SessionLocal()

repo = TicketRepository(db)

service = TicketService(repo)

ticket = service.create_ticket(
    user_id=1,
    ticket_type="Other",
    complaint_message="Testing service layer"
)

print(ticket.ticket_number)

db.close()