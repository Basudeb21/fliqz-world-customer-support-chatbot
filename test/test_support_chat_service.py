# test/test_support_chat_service.py

from app.db.database import (
    SessionLocal
)

from app.repositories.chat_repository import (
    ChatRepository
)

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.services.ticket_service import (
    TicketService
)

from app.services.chat_service import (
    ChatService
)

from app.services.support_chat_service import (
    SupportChatService
)


db = SessionLocal()

chat_repository = ChatRepository(
    db
)

ticket_repository = TicketRepository(
    db
)

ticket_service = TicketService(
    ticket_repository
)

chat_service = ChatService(
    chat_repository,
    ticket_service
)

support_chat_service = (
    SupportChatService(
        chat_repository,
        chat_service
    )
)

response = (
    support_chat_service.process_message(
        user_id=1,
        message="Can I save my filter settings?"
    )
)

print(response)

db.close()