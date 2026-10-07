from memory.conversation_memory import (
    ConversationMemory
)


def test_memory():

    memory = ConversationMemory()

    memory.add_user_message(
        "My flight is from Hyderabad to Delhi."
    )

    memory.add_assistant_message(
        "I can help with your flight."
    )

    assert len(
        memory.get_messages()
    ) == 2


def test_clear_memory():

    memory = ConversationMemory()

    memory.add_user_message(
        "Hello"
    )

    memory.clear()

    assert len(
        memory.get_messages()
    ) == 0