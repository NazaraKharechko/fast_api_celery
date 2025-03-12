import requests
import datetime
from celery import shared_task
from .models import CityWeather
API_KEY = 'f2b4ac37694e1c98b186f2200b970320'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@shared_task
def update_weather():
    """Оновлює погоду для 5 міст та зберігає у PostgreSQL"""
    cities = ["Lviv", "Kyiv", "Odessa", "Kharkiv", "Dnipro"]

    for city in cities:
        PARAMS = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        r = requests.get(url=BASE_URL, params=PARAMS)
        res = r.json()

        if 'main' in res:
            temp = res['main']['temp']
            description = res['weather'][0]['description']
            icon = res['weather'][0]['icon']
            date = datetime.date.today()

            CityWeather.objects.update_or_create(
                city=city,
                defaults={'temp': temp, 'description': description, 'icon': icon, 'date': date}
            )

    return "Weather updated for 5 cities"

"""Оновлення даних кожних 30хв celery"""