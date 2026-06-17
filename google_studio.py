from google import genai
from dotenv import load_dotenv
import os

import streamlit as st


api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

def get_response(prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    return response.text
