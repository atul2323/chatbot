import os
import json
import sys
import subprocess

# Automatically install the correct package inside Streamlit's environment if missing
try:
    import google.genai as genai
    from google.genai import types
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-genai"])
    import google.genai as genai
    from google.genai import types

import streamlit as st

working_dir=os.path.dirname(os.path.abspath(__file__))
config_data=json.load(open(f"{working_dir}/config.json"))
GEMINI_API_KEY=config_data["GEMINI_API_KEY"]

client = genai.Client(api_key=GEMINI_API_KEY)


#streamlib

st.set_page_config(page_title="Flash 2.5",page_icon="💬",layout="centered")
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

st.title("GEMINI 🤖")
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt=st.chat_input("kya hua bolo babu")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})


    formatted_contents = [
        types.Content(
            role="user" if msg["role"] == "user" else "model", 
            parts=[types.Part.from_text(text=msg["content"])]
        )
        for msg in st.session_state.chat_history
    ]
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=formatted_contents,
        config=types.GenerateContentConfig(system_instruction="you are a helpful chatbot")
    )
    
    assistant_response = response.text
    
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)