from fastapi import FastAPI
from logic import categorize_task

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Task Categorizer is running"}

@app.post("/analyze")
def analyze(task_description: str):
    category = categorize_task(task_description)
    return {"description": task_description, "category": category}