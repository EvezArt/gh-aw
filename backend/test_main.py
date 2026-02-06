import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_router_webhook():
    response = client.post("/router/webhook", json={"source": "stripe", "payload": {"refund": 0.1}})
    assert response.status_code == 200
    assert response.json()["action"] == "HARDEN"

def test_cells_slice():
    response = client.post("/cells/slice", json={"amount": 100})
    assert response.status_code == 200
    assert "tax" in response.json()