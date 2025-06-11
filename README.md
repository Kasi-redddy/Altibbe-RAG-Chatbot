# Altibbe-RAG-Chatbot


Altibbe RAG Chatbot is a local Retrieval-Augmented Generation (RAG) system that allows you to upload PDFs, automatically ingest them into a vector database using ChromaDB, and chat with the content using a locally hosted LLaMA3 model via Ollama. It integrates **Streamlit** as the frontend, **FastAPI** as the backend, **ChromaDB** for vector storage, and **n8n** for file upload automation.

---

## 🚀 Features

- ✅ Upload and ingest PDF files
- ✅ Local vector store with ChromaDB
- ✅ Embeddings via `all-MiniLM-L6-v2`
- ✅ Local LLaMA3 model with Ollama
- ✅ Ask questions about your PDF content
- ✅ Automated ingestion using n8n
- ✅ Runs entirely offline — privacy-first

---

## 🗂️ Project Structure
altibbe-rag-chatbot/
│
├── app.py # Streamlit frontend
├── backend.py # FastAPI backend
├── utils.py # PDF loader and embedding
├── rag-chatbot-workflow.json # n8n automation workflow
├── requirements.txt # Dependencies list
└── README.md # This file


---

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/altibbe-rag-chatbot.git
cd altibbe-rag-chatbot

2. Create Virtual Environment

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

3.Install Dependencies

pip install -r requirements.txt

4. Pull and Start Ollama (LLaMA3)

ollama pull llama3
ollama run llama3


Running the Project
Start FastAPI Backend

uvicorn backend:app --reload --port 8000
Start Streamlit Frontend (in another terminal)

streamlit run app.py
Open your browser at: http://localhost:8501

Automate PDF Upload with n8n
1. Start n8n (first install via npm install n8n -g if needed)

npx n8n


2. Import Workflow

Open http://localhost:5678

Click on the top-left menu → "Import Workflow"

Upload the file rag-chatbot-workflow.json

Update the Read PDF node with your actual file path

Run the workflow to upload PDF via FastAPI

Tech Stack
Streamlit

FastAPI

ChromaDB

Ollama

LLaMA3

n8n

Sentence Transformers

Author
Kottapalle Kasi Visweswerreddy
🛠\ AI + Automation Enthusiast
