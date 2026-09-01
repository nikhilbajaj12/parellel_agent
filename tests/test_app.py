from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities_list():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)  # Activities are returned as a dict
    assert len(data) > 0

def test_signup_for_activity_success():
    # Use an existing activity from the app: "Chess Club"
    email = "teststudent@example.com"
    response = client.post("/activities/Chess Club/signup", params={"email": email})
    assert response.status_code == 200
    data = response.json()
    assert data.get("message") == f"Signed up {email} for Chess Club"

    # Verify participant was added
    response = client.get("/activities")
    activities = response.json()
    assert email in activities["Chess Club"]["participants"]

def test_signup_for_activity_failure():
    response = client.post("/activities/NonExistentActivity/signup", params={"email": "teststudent@example.com"})
    assert response.status_code == 404
    data = response.json()
    assert data.get("detail") == "Activity not found"
