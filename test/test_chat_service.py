# test/test_chat_service.py
from app.db.database import SessionLocal

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.services.ticket_service import (
    TicketService
)

from app.services.chat_service import (
    ChatService
)

from app.repositories.chat_repository import(
    ChatRepository
)


db = SessionLocal()

ticket_repo = TicketRepository(
    db
)

chat_repository = ChatRepository(
    db
)

ticket_service = TicketService(
    ticket_repo
)

chat_service = ChatService(
    chat_repository,
    ticket_service
)


response = (
    chat_service.process_message(
        user_id=1,
        message="My payment was deducted but premium was not activated"
    )
)

print(response)

db.close()