
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "ollama"),
    base_url=os.getenv(
        "OPENAI_BASE_URL",
        "http://host.docker.internal:11434/v1"
    )
)

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


@app.get("/")
def home():
    return {"message": "Agentic AI API is running"}


@app.get("/agent")
def agent(query: str):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return {
        "response": response.choices[0].message.content
    }
