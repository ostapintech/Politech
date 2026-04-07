import pytest
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator


# Фікстура для налаштування API клієнта
@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    # Вкажіть URL, на якому запущено ваш FastAPI додаток
    request_context = playwright.request.new_context(base_url="http://127.0.0.1:8000")
    yield request_context
    request_context.dispose()


def test_analyze_bug_task(api_request_context: APIRequestContext):
    response = api_request_context.post(
        "/analyze",
        params={"task_description": "У мене виникає баг при вході"}
    )

    assert response.ok
    assert response.json()["category"] == "Bug"


def test_analyze_urgent_deadline(api_request_context: APIRequestContext):
    response = api_request_context.post(
        "/analyze",
        params={
            "task_description": "Зробити звіт",
            "deadline": "2026-04-08"
        }
    )

    assert response.ok
    assert response.json()["category"] == "Extreme Urgent"