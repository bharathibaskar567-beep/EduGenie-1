import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓"
)

st.title("🎓 EduGenie")
st.subheader("Google Gemini Powered Learning Assistant")

st.write("Ask any educational question and EduGenie will help you understand it.")

question = st.text_area(
    "Enter your question:",
    placeholder="Example: Explain Python loops in simple words"
)

if st.button("Ask EduGenie 🤖"):

    if question.strip():

        with st.spinner("EduGenie is thinking..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )

        st.success("Answer")
        st.write(response.text)

    else:
        st.warning("Please enter a question.")