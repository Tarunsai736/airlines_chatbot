import streamlit as st

from core.chatbot import ask_gemini

from guardrails.airline_guardrail import (
    guardrail_response
)

from memory.conversation_memory import (
    ConversationMemory
)

from services.fallback import (
    fallback_response,
    needs_fallback
)

from services.escalation import (
    needs_escalation,
    needs_model_escalation
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Airline AI Assistant",
    page_icon="✈️",
    layout="centered"
)


# --------------------------------------------------
# SESSION MEMORY
# --------------------------------------------------

if "memory" not in st.session_state:

    st.session_state.memory = (
        ConversationMemory()
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("✈️ Airline AI")

    st.write(
        "Your AI-powered airline "
        "customer support assistant."
    )

    st.divider()

    st.subheader("I can help with:")

    st.write("✈️ Flights")
    st.write("🎫 Tickets & bookings")
    st.write("🧳 Baggage")
    st.write("🛫 Check-in")
    st.write("🚪 Boarding")
    st.write("⏰ Flight delays")
    st.write("💰 Refunds")
    st.write("🏨 Airport information")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.memory.clear()

        st.rerun()


# --------------------------------------------------
# MAIN UI
# --------------------------------------------------

st.title("✈️ Airline AI Assistant")

st.caption(
    "Ask me anything about flights, baggage, "
    "check-in, bookings and airline services."
)


# --------------------------------------------------
# DISPLAY PREVIOUS MESSAGES
# --------------------------------------------------

for message in (
    st.session_state.memory.get_messages()
):

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

user_message = st.chat_input(
    "Ask your airline question..."
)


if user_message:

    # Show user message

    with st.chat_message("user"):

        st.write(user_message)


    # ------------------------------------------------
    # GUARDRAIL
    # ------------------------------------------------

    blocked_response = guardrail_response(
        user_message
    )


    if blocked_response:

        response = blocked_response


    # ------------------------------------------------
    # ESCALATION
    # ------------------------------------------------

    elif needs_escalation(
        user_message
    ):

        response = escalation_response()


    # ------------------------------------------------
    # GEMINI
    # ------------------------------------------------

    else:

        try:

            with st.spinner(
                "✈️ Checking your request..."
            ):

                response = ask_gemini(
                    user_message,
                    st.session_state.memory
                    .get_messages()
                )


        except Exception:

            response = (
                "⚠️ I'm temporarily unable to "
                "process your request.\n\n"
                "Please try again in a moment."
            )


    # ------------------------------------------------
    # MODEL ESCALATION
    # ------------------------------------------------

    if needs_model_escalation(response):

        response = escalation_response()


    # ------------------------------------------------
    # FALLBACK
    # ------------------------------------------------

    elif needs_fallback(response):

        response = fallback_response()


    # ------------------------------------------------
    # SAVE MEMORY
    # ------------------------------------------------

    st.session_state.memory.add_user_message(
        user_message
    )

    st.session_state.memory.add_assistant_message(
        response
    )


    # ------------------------------------------------
    # DISPLAY RESPONSE
    # ------------------------------------------------

    with st.chat_message("assistant"):

        st.write(response)