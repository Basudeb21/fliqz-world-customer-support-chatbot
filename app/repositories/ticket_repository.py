# app/repositories/ticket_repository.py
from sqlalchemy.orm import Session

from app.models.report_ticket import ReportTicket


class TicketRepository:

    def __init__(self, db: Session):

        self.db = db


    def create_ticket(
        self,
        ticket_number,
        user_id,
        ticket_type,
        complaint_message
    ):

        ticket = ReportTicket(
            ticket_number=ticket_number,
            user_id=user_id,
            ticket_type=ticket_type,
            complaint_message=complaint_message
        )

        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)

        return ticket


    def get_ticket(
        self,
        ticket_id
    ):

        return (
            self.db.query(
                ReportTicket
            )
            .filter(
                ReportTicket.id == ticket_id
            )
            .first()
        )


    def update_status(
        self,
        ticket_id,
        status
    ):

        ticket = (
            self.db.query(
                ReportTicket
            )
            .filter(
                ReportTicket.id == ticket_id
            )
            .first()
        )

        if not ticket:
            return None

        ticket.status = status

        self.db.commit()
        self.db.refresh(ticket)

        return ticket
    
def get_user_tickets(
    self,
    user_id
):

    return (
        self.db.query(
            ReportTicket
        )
        .filter(
            ReportTicket.user_id == user_id
        )
        .order_by(
            ReportTicket.id.desc()
        )
        .all()
    )