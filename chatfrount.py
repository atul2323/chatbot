import streamlit as st
from google_studio import get_response

st.title("🤖 AI Chatbot")

user_input = st.text_input("Enter your message")

if st.button("Send"):

    if user_input:

        response = get_response(user_input)

        st.write("### Bot:")
        st.write(response)