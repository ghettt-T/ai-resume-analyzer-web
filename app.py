import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
st.title("🚀AI Resume Analyzer")
uploaded_file = st.file_uploader(
"Upload your resume",
type=["pdf"]
)
if uploaded_file is not None:
    reader= PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        text=page.extract_text()
        if text:
            resume_text  +=text
            if st.button("Analyze Resume"):
                with st.spinner("Analyzing..."):
                    response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    input=f"""
                    Youare an expert technical recruiter
Analyze this resume and provide:
✅Strengths
  ❌Weaknesses
⚒️Improvement Suggestions
 🎯Best suited roles
    Resume: 
    {resume_text}
                    """
                    )
                    st.write(response.output_text)