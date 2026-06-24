# app/models/support_chat.py

from sqlalchemy import (
    Column,
    BigInteger,
    Text,
    Enum,
    DateTime
)

from sqlalchemy.sql import func

from app.db.base import Base


class SupportChat(Base):

    __tablename__ = "support_chat"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    user_id = Column(
        BigInteger,
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )

    role = Column(
        Enum(
            "USER",
            "SUPPORT_BOT"
        ),
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )