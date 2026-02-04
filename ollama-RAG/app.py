from fastapi import FastAPI
import chromadb
import ollama
import os
import logging
import dotenv
dotenv.load_dotenv()
app = FastAPI()
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
MODEL_NAME =os.getenv("MODEL_NAME", "probelem")
logging.info(f"Using model: {MODEL_NAME}") #f" " --> ` `

@app.post("/query")
def query(q: str):
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    answer = ollama.generate(
        model=MODEL_NAME,
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}
@app.post("/add")
def add_knowledge(text: str):
    """add knowledge to the vector database
     Args:
         text (str): text to add to the vector database
     Returns:
         dict: status of the operation
    """
    try:
        import uuid
        doc_id = str(uuid.uuid4())
        collection.add(documents=[text], ids=[doc_id])  
        return {"status": "success", "id": doc_id}
    except Exception as e:
        return {"status": "error", "message": str(e)}

#liveness probe
@app.get("/health")
def health_check():
    return {"status": "ok"}