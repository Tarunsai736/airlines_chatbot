from google import genai

from config.settings import GEMINI_API_KEY
from core.prompts import AIRLINE_INSTRUCTIONS


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def ask_gemini(
    user_message: str,
    conversation_history=None
) -> str:

    history_text = ""

    if conversation_history:

        for message in conversation_history:

            history_text += (
                f"{message['role']}: "
                f"{message['content']}\n"
            )

    prompt = f"""
{AIRLINE_INSTRUCTIONS}

CONVERSATION HISTORY:

{history_text}

CURRENT USER MESSAGE:

{user_message}

Respond to the user.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text.strip()