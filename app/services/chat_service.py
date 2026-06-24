# app/services/chat_service.py
from app.rag.retriever import (
    retrieve_context
)

from app.llm.response_generator import (
    generate_reply
)

from app.tickets.classifier import (
    classify_ticket
)

from app.services.ticket_service import (
    TicketService
)

from app.repositories.chat_repository import (
    ChatRepository
)

from app.memory.memory_manager import (
    MemoryManager
)


class ChatService:

    def __init__(
        self,
        chat_repository: ChatRepository,
        ticket_service: TicketService
    ):

        self.chat_repository = (
            chat_repository
        )

        self.ticket_service = (
            ticket_service
        )

        self.memory_manager = (
            MemoryManager()
        )


    def process_message(
        self,
        user_id: int,
        message: str
    ):

        messages = (
            self.chat_repository
            .get_recent_messages(
                user_id=user_id
            )
        )

        history = (
            self.memory_manager
            .format_history(
                messages
            )
        )

        retrieval_query = (
            self.memory_manager
            .build_retrieval_query(
                history=history,
                message=message
            )
        )

        context = retrieve_context(
            retrieval_query
        )
        
        if context:

            response = generate_reply(
                question=message,
                history=history,
                context=context
            )

            return {
                "type": "CHAT",
                "response": response
            }

        category = classify_ticket(
            message
        )

        ticket = (
            self.ticket_service
            .create_ticket(
                user_id=user_id,
                ticket_type=category,
                complaint_message=message
            )
        )

        return {
            "type": "TICKET",
            "ticket_number": ticket.ticket_number,
            "category": category,
            "response": (
                f"I couldn't find a matching answer.\n\n"
                f"Ticket Number: {ticket.ticket_number}\n"
                f"Category: {category}"
            )
        }