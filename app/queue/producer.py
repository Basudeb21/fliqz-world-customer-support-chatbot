# app/queue/producer.py
import json

from app.queue.redis_client import (
    redis_client
)

from app.core.config import settings


def publish_chat_message(
    user_id,
    message
):

    payload = {
        "user_id": user_id,
        "message": message
    }

    redis_client.xadd(
        settings.REDIS_CHAT_STREAM,
        {
            "data": json.dumps(
                payload
            )
        }
    )