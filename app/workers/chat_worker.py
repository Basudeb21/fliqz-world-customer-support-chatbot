# app/workers/chat_worker.py
import json

from app.queue.redis_client import (
    redis_client
)

from app.queue.consumer import (
    create_consumer_group
)

from app.core.config import settings

from app.db.database import (
    SessionLocal
)

from app.repositories.chat_repository import (
    ChatRepository
)

from app.services.chat_service import (
    ChatService
)

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.services.ticket_service import (
    TicketService
)


create_consumer_group()


while True:

    messages = redis_client.xreadgroup(
        groupname=settings.REDIS_CONSUMER_GROUP,
        consumername=settings.REDIS_CONSUMER_NAME,
        streams={
            settings.REDIS_CHAT_STREAM: ">"
        },
        count=1,
        block=5000
    )

    if not messages:
        continue

    for _, entries in messages:

        for message_id, fields in entries:

            payload = json.loads(
                fields["data"]
            )

            user_id = payload["user_id"]
            message = payload["message"]

            db = SessionLocal()

            try:

                ticket_repository = (
                    TicketRepository(db)
                )

                ticket_service = (
                    TicketService(
                        ticket_repository
                    )
                )

                chat_repository = (
                    ChatRepository(db)
                )

                chat_service = (
                    ChatService(
                        chat_repository,
                        ticket_service
                    )
                )

                result = (
                    chat_service
                    .process_message(
                        user_id=user_id,
                        message=message
                    )
                )

                print(result)

            finally:

                db.close()

            redis_client.xack(
                settings.REDIS_CHAT_STREAM,
                settings.REDIS_CONSUMER_GROUP,
                message_id
            )