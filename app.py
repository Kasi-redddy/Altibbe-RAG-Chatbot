import streamlit as st
import requests

st.set_page_config(page_title="Altibbe RAG Chatbot", layout="centered")

st.title("💬 Altibbe RAG Chatbot")

uploaded = st.file_uploader("📄 Upload a PDF", type=["pdf"])
if uploaded:
    with st.spinner("Uploading..."):
        response = requests.post(
            "http://localhost:8000/upload",
            files={"file": (uploaded.name, uploaded, "application/pdf")}
        )
    if response.status_code == 200:
        st.success("File uploaded and processed!")

query = st.text_input("Ask something about the PDF:")

if query:
    with st.spinner("Thinking..."):
        res = requests.post("http://localhost:8000/query", json={"query": query})
        if res.status_code == 200:
            st.markdown("#### 🤖 Answer:")
            st.write(res.json()["answer"])
        else:
            st.error("Something went wrong.")
