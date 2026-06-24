# app/api/ticket.py
from typing import List

from fastapi import APIRouter

from app.db.database import SessionLocal

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.schemas.ticket_schema import (
    TicketResponse
)


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.get(
    "/{ticket_id}",
    response_model=TicketResponse
)
def get_ticket(
    ticket_id: int
):

    db = SessionLocal()

    try:

        repository = TicketRepository(
            db
        )

        return repository.get_ticket(
            ticket_id
        )

    finally:

        db.close()


@router.get(
    "/user/{user_id}",
    response_model=List[TicketResponse]
)
def get_user_tickets(
    user_id: int
):

    db = SessionLocal()

    try:

        repository = TicketRepository(
            db
        )

        return (
            repository
            .get_user_tickets(
                user_id
            )
        )

    finally:

        db.close()