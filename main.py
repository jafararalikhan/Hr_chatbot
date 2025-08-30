import json
import os
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
assert HUGGINGFACE_API_KEY, "Missing your HuggingFace API key in .env!"

# Load employee data
with open("employees.json") as f:
    employees = json.load(f)["employees"]

# Load embedder
model = SentenceTransformer("all-MiniLM-L6-v2")
emp_texts = [
    f"{e['name']} {', '.join(e['skills'])} {e['experience_years']} years {', '.join(e['projects'])} {e['availability']}"
    for e in employees
]
emp_embeddings = model.encode(emp_texts)

# FastAPI setup
app = FastAPI()

class ChatQuery(BaseModel):
    query: str

def search_employees(query: str, top_k=3):
    q_emb = model.encode([query])[0]
    sims = np.dot(emp_embeddings, q_emb) / (np.linalg.norm(emp_embeddings, axis=1) * np.linalg.norm(q_emb) + 1e-7)
    top_ids = np.argsort(sims)[::-1][:top_k]
    results = [employees[i] for i in top_ids if sims[i] > 0.5]
    return results

def generate_response(prompt: str):
    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 180, "return_full_text": False}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            return response.json()[0]['generated_text']
        except Exception:
            return "Couldn't parse LLM response."
    return "Error from LLM API: " + response.text

@app.post("/chat")
def chat(q: ChatQuery):
    matches = search_employees(q.query)
    if not matches:
        return {"answer": "No suitable employees found for your query."}
    desc = "\n".join([
        f"{e['name']} — Skills: {', '.join(e['skills'])}; Projects: {', '.join(e['projects'])}; Experience: {e['experience_years']} years; Availability: {e['availability']}"
        for e in matches
    ])
    prompt = (
        f"HR is looking for: {q.query}\n"
        f"Matching employees:\n{desc}\n"
        f"Write a friendly and professional HR recommendation explaining why each person fits."
    )
    answer = generate_response(prompt)
    return {"answer": answer, "matches": matches}

@app.get("/employees/search")
def employee_search(skill: str = None, project: str = None):
    results = [
        e for e in employees
        if (not skill or skill.lower() in [s.lower() for s in e["skills"]])
        and (not project or project.lower() in [p.lower() for p in e["projects"]])
    ]
    return {"employees": results}
