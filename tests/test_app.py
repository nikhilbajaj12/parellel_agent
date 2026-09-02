import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_fetch_activities_list_succeeds():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Each key should have expected fields
    for key, item in data.items():
        assert key in data
        assert "description" in item
        assert "schedule" in item


def test_signup_for_activity_succeeds():
    # Use an existing activity from the data
    existing_activity = "Chess Club"
    email = "testuser@example.com"
    response = client.post(f"/activities/{existing_activity}/signup?email={email}")
    assert response.status_code == 200
    json_data = response.json()
    assert "message" in json_data
    assert "signed up" in json_data["message"].lower()


def test_signup_for_nonexistent_activity_fails():
    made_up_activity = "Nonexistent Club"
    email = "testuser@example.com"
    response = client.post(f"/activities/{made_up_activity}/signup?email={email}")
    assert response.status_code == 404
    json_data = response.json()
    assert "detail" in json_data
    assert "not found" in json_data["detail"].lower()
