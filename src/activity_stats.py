def summarize_activities(activities: dict) -> dict:
    """Takes a dictionary of activities and computes participant count, spots left, and full status for each activity.

    Args:
        activities (dict): Dictionary where each key is an activity name and each value is a dict containing
            'description', 'schedule', 'max_participants', and 'participants' (list of emails).

    Returns:
        dict: A dictionary keyed by activity names with each value containing 'participant_count', 'spots_left', and 'is_full'.
    """
    summary = {}
    for activity_name, activity_data in activities.items():
        participant_count = len(activity_data.get('participants', []))
        max_participants = activity_data.get('max_participants', 0)
        spots_left = max_participants - participant_count
        is_full = spots_left <= 0
        summary[activity_name] = {
            'participant_count': participant_count,
            'spots_left': spots_left,
            'is_full': is_full
        }
    return summary
