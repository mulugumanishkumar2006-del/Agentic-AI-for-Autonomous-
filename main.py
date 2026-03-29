from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.agents.orchestrator import run_workflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    input: str

@app.post("/run")
def run(req: Request):
    result = run_workflow(req.input)
    return {"result": result}

@app.get("/")
def home():
    return {"message": "AutoFlow AI Running 🚀"}