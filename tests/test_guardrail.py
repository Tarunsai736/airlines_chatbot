from guardrails.airline_guardrail import (
    classify_airline_intent
)


def test_airline_question():

    assert classify_airline_intent(
        "What is my baggage allowance?"
    )


def test_non_airline_question():

    assert not classify_airline_intent(
        "How do I write Python?"
    )