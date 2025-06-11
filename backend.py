from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
from utils import extract_text_from_pdf
import chromadb
import ollama
import os

app = FastAPI()

# Enable CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup ChromaDB (no server needed)
client = chromadb.PersistentClient(path="db")
collection = client.get_or_create_collection(name="altibbe")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    os.remove(file_path)

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = embedding_model.encode(chunks).tolist()
    ids = [f"doc_{i}" for i in range(len(chunks))]

    collection.add(documents=chunks, embeddings=embeddings, ids=ids)
    return {"status": "uploaded", "chunks": len(chunks)}

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    user_question = data.get("query", "")

    question_embedding = embedding_model.encode(user_question).tolist()

    results = collection.query(query_embeddings=[question_embedding], n_results=3)
    documents = results["documents"][0]
    context = "\n".join(documents)

    prompt = f"Answer the question based on the context:\n\nContext:\n{context}\n\nQuestion: {user_question}"

    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": prompt}
    ])

    return {"answer": response["message"]["content"]}
