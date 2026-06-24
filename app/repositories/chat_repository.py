# app/repositories/chat_repository.py

from sqlalchemy.orm import Session

from app.models.support_chat import SupportChat


class ChatRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def save_message(
        self,
        user_id,
        message,
        role
    ):

        chat = SupportChat(
            user_id=user_id,
            message=message,
            role=role
        )

        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)

        return chat

    def get_chat_history(
        self,
        user_id,
        limit=20
    ):

        return (
            self.db.query(
                SupportChat
            )
            .filter(
                SupportChat.user_id == user_id
            )
            .order_by(
                SupportChat.id.desc()
            )
            .limit(limit)
            .all()
        )

    def get_recent_messages(
        self,
        user_id,
        limit=10
    ):

        return (
            self.db.query(
                SupportChat
            )
            .filter(
                SupportChat.user_id == user_id
            )
            .order_by(
                SupportChat.id.desc()
            )
            .limit(limit)
            .all()
        )