Weather API with Django, Celery, and PostgreSQL

📌 Опис проекту

Цей проект - веб-додаток для отримання даних про погоду з API OpenWeather. Реалізовано RESTful API, використовуючи Django REST framework, а також автоматичне оновлення даних через Celery та Redis. Дані зберігаються в PostgreSQL.

🚀 Функціонал

Отримання погоди в реальному часі через REST API.

Збереження даних у базу PostgreSQL.

Автоматичне оновлення погоди через Celery.

Використання Redis як брокера задач для Celery.

🛠️ Технології

Python 3

Django 4

Django REST Framework

PostgreSQL

Celery + Redis

OpenWeather API

📥 Встановлення

1️⃣ Клонуйте репозиторій

git clone https://github.com/yourusername/weather-django.git
cd weather-django

2️⃣ Створіть віртуальне середовище

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3️⃣ Встановіть залежності

pip install -r requirements.txt

4️⃣ Налаштуйте базу даних PostgreSQL

Створіть .env файл і вкажіть:

DB_NAME=weather_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

5️⃣ Міграція бази даних

python manage.py migrate

6️⃣ Запустіть сервер

python manage.py runserver

API буде доступний за адресою: http://127.0.0.1:8000/api/weather/<city>/