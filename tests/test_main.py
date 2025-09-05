import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_add():
    # TODO: add more edge cases (negatives, large values, zero)
    r = client.post("/add", json={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["sum"] == 5
