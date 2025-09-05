from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CI/CD K8s Demo", version="0.1.0")

class AddRequest(BaseModel):
    a: int
    b: int

@app.get("/health")
def health():
    return {"status": "ok"}

# TODO: Implement: read two numbers and return their sum
@app.post("/add")
def add_numbers(req: AddRequest):
    """
    TODO:
    - return {"sum": <a+b>}
    - add basic input validation if you like
    """
    return {"sum": req.a + req.b}
