import os
import anthropic
from fastapi import FastAPI

ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY")

app = FastAPI(
    title="Claude AI API",
    description="FastAPI + Claude AI — built by Akarshit Sharma",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Claude AI API is running", "docs": "/docs"}

@app.get("/hello")
def hello():
    return {"message": "Hello, Ak!"}

@app.get("/ask")
def ask(question: str):
    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return {"question": question, "answer": message.content[0].text}
