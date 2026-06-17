from google import genai
import streamlit as st
api_key=st.secrets["AQ.Ab8RN6IOInd9SJOhdhUwuEcm0ZzQv5bxCLIKvn6bdx1Mia2eVQ"]

client = genai.Client(api_key=api_key)

while True:
    text = input("You: ")

    if text.lower() == "bye":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
    )

    print("Chatbot:", response.text)
