import streamlit as st
from google_studio import get_response

st.title("🤖 Gemini AI Chatbot")

prompt = st.chat_input("Type your message...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    response = get_response(prompt)

    with st.chat_message("assistant"):
        st.write(response)
