from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities_list():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_for_activity_success():
    activity = "Programming Class"
    email = "example@example.com"
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert response.status_code == 200
    data = response.json()
    assert data.get("message") == f"Signed up {email} for {activity}"

def test_signup_for_nonexistent_activity_failure():
    activity = "made_up_activity"
    response = client.post(f"/activities/{activity}/signup", params={"email": "example@example.com"})
    assert response.status_code == 404
    data = response.json()
    assert data.get("detail") == "Activity not found"
