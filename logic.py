from datetime import datetime


def get_days_until_deadline(deadline_str: str) -> int:
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        delta = deadline - datetime.now()
        return delta.days + 1
    except ValueError:
        return -999


def categorize_task(text: str, deadline_str: str = None) -> str:
    text = text.lower()

    if deadline_str:
        days_left = get_days_until_deadline(deadline_str)
        if 0 <= days_left <= 2:
            return "Extreme Urgent"

    if not text.strip():
        return "Invalid"
    if "терміново" in text or "urgent" in text:
        return "High Priority"
    if "баг" in text or "error" in text:
        return "Bug"
    return "Final Main Task"
