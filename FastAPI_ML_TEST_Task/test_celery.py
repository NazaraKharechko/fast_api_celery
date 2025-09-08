import csv
import requests
from celery import Celery

# 1. Ініціалізація Celery
app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",   # або rabbitmq: "pyamqp://guest@localhost//"
    backend="redis://localhost:6379/0"
)

# 2. Завдання для Celery
@app.task
def fetch_and_save_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    users = response.json()

    # Зберігаємо у CSV
    with open("users.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "email"])  # заголовки
        for u in users:
            writer.writerow([u["id"], u["name"], u["email"]])

    return f"Saved {len(users)} users to users.csv"
