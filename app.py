import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
st.title("🚀AI Resume Analyzer")
uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

resume_text = ""

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text


# 👇 BUTTON LIVES HERE (not nested)
if st.button("Analyze Resume"):
    with st.spinner("Analyzing..."):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an expert technical recruiter."},
                {"role": "user", "content": resume_text}
            ]
        )

        st.write(response.choices[0].message.content)
