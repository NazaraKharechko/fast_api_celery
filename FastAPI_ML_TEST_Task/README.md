# 🚀 ToDo API + Frontend + Celery

Проєкт демонструє:
- **REST API** на FastAPI для управління списком задач (to-do list)
- **Фронтенд (HTML)** для перегляду та додавання задач
- **Celery + Redis** для фонових завдань (приклад — завантаження користувачів з публічного API та збереження у CSV)
- **Unit-тести** з pytest

---

## ⚙️ Стек
- Python 3.10+
- FastAPI
- Uvicorn
- Celery
- Redis
- Requests
- Pytest
- Jinja2 (якщо потрібні шаблони)

---
1. Встанови залежності:
   ```bash
   pip install -r requirements.txt
   
апусти FastAPI:

uvicorn main:app --reload


Відкрий у браузері:

Swagger: http://127.0.0.1:8000/docs

Фронтенд: http://127.0.0.1:8000/pages/tasks

🔄 Celery

Запуск воркера (якщо без Docker):

celery -A tasks worker --loglevel=info