"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import Response
from fastapi import Header
from collections import deque
import time

# Rate limiting middleware data structure and logic
rate_limits = {}
RATE_LIMIT = 60
WINDOW_SIZE = 60  # seconds

def rate_limit_middleware(request: Request):
    ip = request.client.host
    now = time.time()

    # Initialize deque for this IP if not present
    if ip not in rate_limits:
        rate_limits[ip] = deque()

    # Remove timestamps outside the window
    while rate_limits[ip] and rate_limits[ip][0] <= now - WINDOW_SIZE:
        rate_limits[ip].popleft()

    if len(rate_limits[ip]) >= RATE_LIMIT:
        # Calculate Retry-After
        retry_after = int(rate_limits[ip][0] + WINDOW_SIZE - now)
        # Return HTTP 429 with Retry-After header
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"detail": "Too many requests"},
            headers={"Retry-After": str(retry_after)}
        )

    # Record this request timestamp
    rate_limits[ip].append(now)

@app.post("/api/v2/checkout")
async def checkout(request: Request):
    # Call rate limit middleware
    response = rate_limit_middleware(request)
    if response:
        return response

    return {"status": "ok"}
