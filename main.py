import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

# Ініціалізація МАЄ БУТИ ТУТ
sentry_sdk.init(
    dsn="https://f1c6855bcb25361cfb520cf636ee3032@o4511250818072576.ingest.de.sentry.io/4511250828361808",
    integrations=[FastApiIntegration()],
    traces_sample_rate=1.0,
    debug=True,  # Обов'язково True, щоб побачити помилку в консолі
)
import os
from posthog import Posthog  # Не забудьте: pip install posthog
from fastapi import FastAPI
from logic import categorize_task
from dotenv import load_dotenv
import uuid
import time

load_dotenv()
# 1. Спершу оголошуємо змінну (виправлення вашої помилки)
APP_STATUS = os.getenv("VITE_APP_STATUS", "Development")

# 2. Ініціалізація PostHog (Крок 1 лабораторної) [cite: 145, 146]
posthog_api_key = os.getenv("POSTHOG_API_KEY")
posthog = Posthog(posthog_api_key, host="https://us.i.posthog.com")

app = FastAPI()


@app.get("/")
def read_root():
    # Тепер APP_STATUS доступний
    return {"message": "AI Task Categorizer is running", "status": APP_STATUS}


@app.post("/analyze")
def analyze(task_description: str = "", deadline: str = None, user_id: str = "guest"):
    # 1. Sentry Context
    sentry_sdk.set_user(
        {
            "id": user_id,
            "email": "ostap.zherebtsov.pp.2023@lpnu.ua",
            "username": "Ostap",
        }
    )

    sentry_sdk.add_breadcrumb(
        category="ui",
        message=f"Користувач натиснув аналіз для: {task_description[:15]}...",
        level="info",
    )

    # 2. Validation
    if not task_description:
        raise ValueError("Опис завдання порожній!")

    # 3. Logic & Feature Flags
    category = categorize_task(task_description, deadline)

    # Check PostHog Feature Flag
    # if not posthog.feature_enabled("ai-analysis-enabled", user_id):
    #     return {"error": "AI analysis is currently disabled"}

    # 4. PostHog Event Capture
    posthog.capture(
        distinct_id=user_id,
        event="task_created",
        properties={
            "category": category,
            "status": APP_STATUS,
            "has_deadline": bool(deadline),
        },
    )

    # 5. Return Full Object (To satisfy the tests)
    return {
        "description": task_description,
        "deadline": deadline,
        "category": category,  # This fixes the KeyError
        "env_mode": APP_STATUS,
    }


@app.get("/sentry-debug")
async def trigger_error():
    with sentry_sdk.configure_scope() as scope:
        scope.set_tag("test_id", str(time.time()))  # Унікальний тег
    raise Exception(f"New Unique Error {time.time()}")
