from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_fetch_activities_list():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data


def test_signup_for_activity_success():
    email = "teststudent@mergington.edu"
    activity_name = "Chess Club"
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == f"Signed up {email} for {activity_name}"


def test_signup_for_nonexistent_activity_fails():
    email = "teststudent@mergington.edu"
    activity_name = "MadeUpActivity"
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Activity not found"
