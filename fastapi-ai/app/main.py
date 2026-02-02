import os 
from fastapi import FastAPI
from dotenv import load_dotenv
import google.generativeai as genai
from . import models
load_dotenv()  # loads .env into environment variables
google_api_key=os.getenv("Gemini_API_Key")

app= FastAPI()

@app.get("/")
async def root():
    return {"message":"API is running"}

@app.post('/chat',response_model=models.ChatResponse)
async def chat(request: models.ChatRequest):
    #ai geenration
    response_text="..."
    return models.ChatResponse(response=response_text)