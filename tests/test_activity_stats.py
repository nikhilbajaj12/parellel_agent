import pytest
from src.activity_stats import summarize_activities

def test_summarize_activities():
    activities = {
        'yoga': {
            'description': 'Morning yoga session',
            'schedule': 'Daily 7-8AM',
            'max_participants': 3,
            'participants': ['a@example.com', 'b@example.com']
        },
        'running': {
            'description': 'Evening run',
            'schedule': 'Daily 6-7PM',
            'max_participants': 2,
            'participants': ['c@example.com', 'd@example.com']
        },
        'cycling': {
            'description': 'Weekend cycling',
            'schedule': 'Sat 8AM-10AM',
            'max_participants': 4,
            'participants': ['e@example.com', 'f@example.com', 'g@example.com', 'h@example.com']
        }
    }

    result = summarize_activities(activities)

    assert result['yoga']['participant_count'] == 2
    assert result['yoga']['spots_left'] == 1
    assert result['yoga']['is_full'] is False

    assert result['running']['participant_count'] == 2
    assert result['running']['spots_left'] == 0
    assert result['running']['is_full'] is True

    assert result['cycling']['participant_count'] == 4
    assert result['cycling']['spots_left'] == 0
    assert result['cycling']['is_full'] is True
