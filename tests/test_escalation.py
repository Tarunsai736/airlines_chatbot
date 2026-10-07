from services.escalation import (
    needs_escalation
)


def test_lost_baggage():

    assert needs_escalation(
        "My baggage is lost"
    )


def test_normal_question():

    assert not needs_escalation(
        "What is check-in?"
    )