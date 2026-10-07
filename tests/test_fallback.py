from services.fallback import (
    needs_fallback
)


def test_fallback():

    assert needs_fallback(
        "INSUFFICIENT_INFORMATION"
    )


def test_normal_response():

    assert not needs_fallback(
        "Your baggage allowance depends "
        "on your airline."
    )