from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_checkout_rate_limit_ok():
    for _ in range(60):
        response = client.post("/api/v2/checkout")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    response = client.post("/api/v2/checkout")
    assert response.status_code == 429
    assert "Retry-After" in response.headers
