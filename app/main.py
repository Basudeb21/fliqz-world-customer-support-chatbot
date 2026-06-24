# app/main.py
from fastapi import FastAPI

from app.core.config import settings

from app.api.ticket import (
    router as ticket_router
)

from app.api.chat import (
    router as chat_router
)




app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(
    ticket_router
)

app.include_router(
    chat_router
)


@app.get("/")
def root():

    return {
        "message": "Fliqz AI Support Bot Running"
    }