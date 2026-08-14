def summarize_activities(activities: dict) -> dict:
    """
    Summarize participant statistics for each activity in the activities dictionary.

    Parameters:
    activities (dict): Dictionary keyed by activity name, where each value is a dict with keys:
        - description (str)
        - schedule (str)
        - max_participants (int)
        - participants (list[str]): List of participant emails

    Returns:
    dict: A new dictionary keyed by activity name, where each value is a dict with keys:
        - participant_count (int): Number of participants
        - spots_left (int): Remaining spots available
        - is_full (bool): True if the activity is full, False otherwise
    """
    summary = {}
    for activity_name, activity in activities.items():
        participant_count = len(activity.get('participants', []))
        max_participants = activity.get('max_participants', 0)
        spots_left = max_participants - participant_count
        is_full = spots_left <= 0
        summary[activity_name] = {
            'participant_count': participant_count,
            'spots_left': spots_left,
            'is_full': is_full
        }
    return summary
