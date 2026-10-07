class ConversationMemory:

    def __init__(self, max_messages=20):

        self.messages = []
        self.max_messages = max_messages

    def add_user_message(self, message: str):

        self.messages.append({
            "role": "user",
            "content": message
        })

        self._limit_memory()

    def add_assistant_message(self, message: str):

        self.messages.append({
            "role": "assistant",
            "content": message
        })

        self._limit_memory()

    def _limit_memory(self):

        if len(self.messages) > self.max_messages:

            self.messages = self.messages[
                -self.max_messages:
            ]

    def get_messages(self):

        return self.messages

    def get_context(self):

        context = []

        for message in self.messages:

            context.append(
                f"{message['role']}: "
                f"{message['content']}"
            )

        return "\n".join(context)

    def clear(self):

        self.messages = []