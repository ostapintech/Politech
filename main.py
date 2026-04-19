import os
from fastapi import FastAPI
from logic import categorize_task
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

APP_STATUS = os.getenv("VITE_APP_STATUS", "Development")


@app.get("/")
def read_root():
    return {"message": "AI Task Categorizer is running", "status": APP_STATUS}


@app.post("/analyze")
def analyze(task_description: str, deadline: str = None):
    category = categorize_task(task_description, deadline)
    return {
        "description": task_description,
        "deadline": deadline,
        "category": category,
        "env_mode": APP_STATUS,
    }
