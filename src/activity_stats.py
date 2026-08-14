def summarize_activities(activities: dict) -> dict:
    """Summarize activity participation details.

    Args:
        activities (dict): Dictionary where each key is an activity name and each value is
                            a dict with keys: 'description', 'schedule', 'max_participants', 'participants' (list of emails).

    Returns:
        dict: A new dictionary keyed by activity name. Each value is a dict with keys:
              'participant_count' (int), 'spots_left' (int), and 'is_full' (bool).
    """
    summary = {}
    for activity_name, details in activities.items():
        participant_count = len(details.get('participants', []))
        max_participants = details.get('max_participants', 0)
        spots_left = max_participants - participant_count
        is_full = spots_left <= 0
        summary[activity_name] = {
            'participant_count': participant_count,
            'spots_left': spots_left,
            'is_full': is_full
        }
    return summary
