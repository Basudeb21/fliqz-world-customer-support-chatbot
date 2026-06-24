# app/services/ticket_service.py
from datetime import datetime

from app.repositories.ticket_repository import (
    TicketRepository
)


class TicketService:

    def __init__(
        self,
        ticket_repository: TicketRepository
    ):

        self.ticket_repository = (
            ticket_repository
        )


    def generate_ticket_number(self):

        timestamp = datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )

        return f"FLQ-{timestamp}"


    def create_ticket(
        self,
        user_id,
        ticket_type,
        complaint_message
    ):

        ticket_number = (
            self.generate_ticket_number()
        )

        return (
            self.ticket_repository
            .create_ticket(
                ticket_number=ticket_number,
                user_id=user_id,
                ticket_type=ticket_type,
                complaint_message=complaint_message
            )
        )