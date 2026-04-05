# AI Task Categorizer MVP
## Опис проєкту

Це сервіс на базі FastAPI, який автоматично класифікує текстові завдання користувача за категоріями (Bug, High Priority, Task). Проєкт створено для демонстрації навичок роботи з Git (branching, pull requests)
## Стек технологій

Мова: Python 3.10+

Фреймворк: FastAPI

Контроль версій: Git
## Швидкий старт

 Клонування репозиторію: git clone https://github.com/ostapintech/Politech.git

### Налаштування оточення: 
- python -m venv venv
- source venv/bin/activate  
- pip install fastapi uvicorn pytest pytest-cov

Запуск сервера: uvicorn main:app --reload

Після запуску API буде доступне за адресою: http://127.0.0.1:8000/docs
