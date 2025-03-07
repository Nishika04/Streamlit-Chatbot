import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("💬 AI Chatbot (GPT-4o Mini)")
st.write("Ask me anything!")

user_input = st.text_input("You:", "")

if st.button("Ask"):
    if user_input:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # ✅ Use GPT-4o Mini model
            messages=[{"role": "system", "content": "You are a helpful AI assistant."},
                      {"role": "user", "content": user_input}]
        )
        st.write("🤖 AI:", response.choices[0].message.content)
