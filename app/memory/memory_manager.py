# app/memory/memory_manager.py

class MemoryManager:

    def format_history(
        self,
        messages
    ):

        history = []

        for msg in reversed(messages):

            history.append(
                f"{msg.role}: {msg.message}"
            )

        return "\n".join(history)

    def build_retrieval_query(
        self,
        history: str,
        message: str
    ):

        return f"""
            Conversation History:
            {history}

            Current User Message:
            {message}
        """