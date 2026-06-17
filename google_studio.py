import streamlit as st
from google import genai

# Get API Key from Streamlit Secrets
api_key = "AQ.Ab8RN6JxvRwQYzPl1VmWaU7_ICieiiAsyhfW9dH08lUClUZyZg"

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Page Title
st.title("🤖 Gemini AI Chatbot")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)

# User Input
prompt = st.chat_input("Type your message...")

if prompt:

    # Show user message
    st.session_state.messages.append(("user", prompt))

    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        bot_reply = response.text

        st.session_state.messages.append(("assistant", bot_reply))

        with st.chat_message("assistant"):
            st.write(bot_reply)

    except Exception as e:
        st.error(f"Error: {e}")
