# app/tickets/classifier.py
from app.constants.ticket_keywords import (
    PAYMENT_KEYWORDS,
    REFUND_KEYWORDS,
    ACCOUNT_KEYWORDS,
    ORDER_KEYWORDS,
    PRODUCT_KEYWORDS
)


TICKET_CATEGORIES = [
    "Payment Issue",
    "Order Not Delivered",
    "Account Access Issue",
    "Product Quality Issue",
    "Refund Request",
    "Other"
]


def classify_ticket(message: str):

    message = message.lower()

    if any(
        keyword in message
        for keyword in PAYMENT_KEYWORDS
    ):
        return "Payment Issue"

    if any(
        keyword in message
        for keyword in REFUND_KEYWORDS
    ):
        return "Refund Request"

    if any(
        keyword in message
        for keyword in ACCOUNT_KEYWORDS
    ):
        return "Account Access Issue"

    if any(
        keyword in message
        for keyword in ORDER_KEYWORDS
    ):
        return "Order Not Delivered"

    if any(
        keyword in message
        for keyword in PRODUCT_KEYWORDS
    ):
        return "Product Quality Issue"

    return "Other"