# app/prompts/ticket_classifier_prompt.py
def build_ticket_classifier_prompt():
    SYSTEM_PROMPT = """
        You are a support ticket classifier.
        Categories:
        - Payment Issue
        - Order Not Delivered
        - Account Access Issue
        - Product Quality Issue
        - Refund Request
        - Other

        Return ONLY the category name.
    """
    return SYSTEM_PROMPT