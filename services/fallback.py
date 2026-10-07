def fallback_response():

    return (
        "I'm sorry, but I don't have enough reliable "
        "information to answer that question. "
        "Please check the airline's official website "
        "or contact airline customer support for the "
        "latest information."
    )


def needs_fallback(response: str):

    return (
        "INSUFFICIENT_INFORMATION"
        in response.upper()
    )