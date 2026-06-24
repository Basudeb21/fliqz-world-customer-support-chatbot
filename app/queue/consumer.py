# app/queue/consumer.py

from app.queue.redis_client import (
    redis_client
)

from app.core.config import settings


def create_consumer_group():

    try:

        redis_client.xgroup_create(
            settings.REDIS_CHAT_STREAM,
            settings.REDIS_CONSUMER_GROUP,
            id="0",
            mkstream=True
        )

    except Exception:

        pass