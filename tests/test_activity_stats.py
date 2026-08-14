import pytest
from src.activity_stats import summarize_activities

def test_summarize_activities():
    activities = {
        "Yoga": {
            "description": "Relaxing morning yoga",
            "schedule": "8 AM",
            "max_participants": 3,
            "participants": ["a@example.com", "b@example.com"]
        },
        "Running": {
            "description": "Evening run",
            "schedule": "6 PM",
            "max_participants": 2,
            "participants": ["c@example.com", "d@example.com"]
        },
        "Swimming": {
            "description": "Pool laps",
            "schedule": "5 PM",
            "max_participants": 1,
            "participants": ["e@example.com"]
        }
    }

    result = summarize_activities(activities)

    assert result["Yoga"]["participant_count"] == 2
    assert result["Yoga"]["spots_left"] == 1
    assert result["Yoga"]["is_full"] is False

    assert result["Running"]["participant_count"] == 2
    assert result["Running"]["spots_left"] == 0
    assert result["Running"]["is_full"] is True

    assert result["Swimming"]["participant_count"] == 1
    assert result["Swimming"]["spots_left"] == 0
    assert result["Swimming"]["is_full"] is True
