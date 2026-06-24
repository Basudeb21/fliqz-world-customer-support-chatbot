# app/api/chat.py
from fastapi import APIRouter

from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse
)
from typing import List

from app.schemas.history import (
    ChatHistoryResponse
)
from app.db.database import SessionLocal

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


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "",
    response_model=ChatResponse
)
def send_message(
    request: ChatRequest
):

    db = SessionLocal()

    try:

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

        result = (
            support_chat_service
            .process_message(
                user_id=request.user_id,
                message=request.message
            )
        )

        return ChatResponse(
            type=result["type"],
            response=result["response"]
        )

    finally:

        db.close()

@router.get(
    "/history/{user_id}",
    response_model=List[ChatHistoryResponse]
)
def get_chat_history(
    user_id: int
):

    db = SessionLocal()

    try:

        chat_repository = ChatRepository(
            db
        )

        return (
            chat_repository
            .get_chat_history(
                user_id=user_id
            )
        )

    finally:

        db.close()