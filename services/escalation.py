def needs_escalation(message: str) -> bool:
    """
    Check whether a user message requires human escalation.
    """

    message = message.lower().strip()

    escalation_patterns = [
        # Baggage problems
        "lost baggage",
        "baggage is lost",
        "baggage was lost",
        "baggage has been lost",
        "lost luggage",
        "luggage is lost",
        "luggage was lost",
        "luggage has been lost",
        "missing baggage",
        "baggage is missing",
        "missing luggage",
        "luggage is missing",

        # Refund / payment issues
        "refund",
        "chargeback",
        "fraud",
        "unauthorized payment",

        # Complaints / legal
        "complaint",
        "legal",
        "lawyer",
        "lawsuit",

        # Emergency
        "emergency",
        "medical emergency",
        "injury",
        "security issue",

        # Human support
        "human agent",
        "talk to an agent",
        "talk to agent",
        "speak to an agent",
        "speak to agent",
        "customer support",
        "human support",
    ]

    return any(pattern in message for pattern in escalation_patterns)
def needs_model_escalation(message: str) -> bool:
    """
    Determine whether a message needs escalation
    based on complex or uncertain requests.
    """

    message = message.lower().strip()

    model_escalation_keywords = [
        "complex issue",
        "special assistance",
        "dispute",
        "compensation",
        "legal action",
        "speak to a human",
        "talk to a human",
        "human agent",
        "customer service",
        "customer support",
        "manager",
        "supervisor",
    ]

    return any(
        keyword in message
        for keyword in model_escalation_keywords
    )
def needs_escalation(message: str) -> bool:
    # your existing baggage/refund/emergency checks
    ...


def needs_model_escalation(message: str) -> bool:
    # model/complex-request checks
    ...