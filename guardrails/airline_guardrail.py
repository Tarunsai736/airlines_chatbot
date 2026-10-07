from google import genai
from config.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


AIRLINE_KEYWORDS = [
    "flight",
    "flights",
    "airline",
    "airport",
    "boarding",
    "boarding pass",
    "baggage",
    "luggage",
    "suitcase",
    "check-in",
    "check in",
    "ticket",
    "booking",
    "reservation",
    "departure",
    "arrival",
    "gate",
    "cabin",
    "pilot",
    "aircraft",
    "plane",
    "layover",
    "transit",
    "flight status",
    "cancel flight",
    "cancellation",
    "refund",
]


def obvious_airline_question(message: str) -> bool:
    message = message.lower()

    return any(
        keyword in message
        for keyword in AIRLINE_KEYWORDS
    )


def classify_airline_intent(message: str) -> bool:

    if obvious_airline_question(message):
        return True

    prompt = f"""
You are an intent classifier for an airline customer support chatbot.

Classify the user's message.

Return ONLY:

AIRLINE

or

OTHER

AIRLINE means the question is related to:

- flights
- airlines
- airports
- baggage
- luggage
- boarding
- check-in
- tickets
- reservations
- cancellations
- refunds
- flight delays
- airline procedures
- airline customer support

OTHER means anything outside the airline domain.

User message:

{message}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        result = response.text.strip().upper()

        return result == "AIRLINE"

    except Exception:

        # Fail closed for safety
        return False


def guardrail_response(message: str):

    if classify_airline_intent(message):
        return None

    return (
        "✈️ I'm an airline customer support assistant. "
        "I can only help with airline-related questions such as "
        "flights, baggage, check-in, bookings, cancellations, "
        "refunds, delays, and airport information."
    )