import pytest
from src.activity_stats import summarize_activities

def test_summarize_activities():
    activities = {
        'Yoga': {
            'description': 'Morning yoga session',
            'schedule': '8 AM - 9 AM',
            'max_participants': 3,
            'participants': ['a@example.com', 'b@example.com']
        },
        'Cooking': {
            'description': 'French cooking class',
            'schedule': '10 AM - 11 AM',
            'max_participants': 2,
            'participants': ['c@example.com', 'd@example.com']
        },
        'Dance': {
            'description': 'Evening dance session',
            'schedule': '6 PM - 7 PM',
            'max_participants': 2,
            'participants': ['e@example.com', 'f@example.com', 'g@example.com']
        }
    }

    result = summarize_activities(activities)

    assert result['Yoga']['participant_count'] == 2
    assert result['Yoga']['spots_left'] == 1
    assert result['Yoga']['is_full'] is False

    assert result['Cooking']['participant_count'] == 2
    assert result['Cooking']['spots_left'] == 0
    assert result['Cooking']['is_full'] is True

    assert result['Dance']['participant_count'] == 3
    assert result['Dance']['spots_left'] == -1
    assert result['Dance']['is_full'] is True
