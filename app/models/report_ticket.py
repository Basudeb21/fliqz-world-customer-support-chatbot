# app/models/report_ticket.py
from sqlalchemy import (
    Column,
    BigInteger,
    Text,
    Enum,
    String,
    DateTime
)

from sqlalchemy.sql import func

from app.db.base import Base


class ReportTicket(Base):

    __tablename__ = "report_ticket"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    ticket_number = Column(
        String(30),
        unique=True
    )

    user_id = Column(
        BigInteger,
        nullable=False
    )

    ticket_type = Column(
        Enum(
            'Payment Issue',
            'Order Not Delivered',
            'Account Access Issue',
            'Product Quality Issue',
            'Refund Request',
            'Other'
        ),
        nullable=False
    )

    complaint_message = Column(
        Text,
        nullable=False
    )

    status = Column(
        Enum(
            'REPORTED',
            'PENDING',
            'ACCEPTED',
            'REJECTED',
            'CLOSED'
        ),
        default='REPORTED',
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )