# app/services/support_chat_service.py

from app.repositories.chat_repository import (
    ChatRepository
)

from app.services.chat_service import (
    ChatService
)


class SupportChatService:

    def __init__(
        self,
        chat_repository: ChatRepository,
        chat_service: ChatService
    ):

        self.chat_repository = (
            chat_repository
        )

        self.chat_service = (
            chat_service
        )


    def process_message(
        self,
        user_id: int,
        message: str
    ):

        # Save USER message
        self.chat_repository.save_message(
            user_id=user_id,
            message=message,
            role="USER"
        )

        # Generate response
        result = (
            self.chat_service
            .process_message(
                user_id=user_id,
                message=message
            )
        )

        # Save BOT response
        self.chat_repository.save_message(
            user_id=user_id,
            message=result["response"],
            role="SUPPORT_BOT"
        )

        return result