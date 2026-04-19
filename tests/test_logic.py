from logic import categorize_task, get_days_until_deadline
from datetime import datetime, timedelta


def test_get_days_until_deadline_valid():
    future_date = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
    assert get_days_until_deadline(future_date) == 2


def test_categorize_extreme_urgent():
    near_deadline = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    assert categorize_task("Завдання", near_deadline) == "Extreme Urgent"


def test_invalid_date_format():
    assert get_days_until_deadline("01-01-2026") == -999
