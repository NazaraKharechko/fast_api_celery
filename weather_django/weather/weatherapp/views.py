from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime


def get_weather(city):
    """
    Отримує поточну погоду для вказаного міста за допомогою OpenWeatherMap API.

    :param city: Назва міста
    :return: Словник з інформацією про погоду (опис, температура, іконка тощо)
    """
    API_KEY = ''  # ваш API-ключ з OpenWeatherMap
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': API_KEY, 'units': 'metric', 'lang': 'en'}

    response = requests.get(url=URL, params=PARAMS)
    if response.status_code == 200:
        res = response.json()
        return {
            'city': city,
            'description': res['weather'][0]['description'],
            'icon': res['weather'][0]['icon'],
            'temp': res['main']['temp'],
            'day': datetime.date.today()
        }
    else:
        return {
            'city': city,
            'description': 'City not found',
            'icon': '',
            'temp': 'N/A',
            'day': datetime.date.today()
        }


def index(request):
    """
    Відображає головну сторінку з інформацією про погоду для вибраного міста.

    :param request: HTTP-запит
    :return: Відрендерений HTML-шаблон з погодою
    """
    city = request.POST.get('city', 'Lviv')  # Отримуємо місто або 'Lviv' за замовчуванням
    weather = get_weather(city)
    return render(request, 'weatherapp/index.html', weather)


def all_index(request):
    """
    Відображає погоду для кількох міст, включаючи місто, яке ввів користувач.

    :param request: HTTP-запит
    :return: Відрендерений HTML-шаблон з погодою для кількох міст
    """
    cities = ['Lviv', 'Kyiv', 'Odessa', 'London', 'Dnipro']
    user_city = request.POST.get('city')

    if user_city and user_city not in cities:
        cities.insert(0, user_city)

    weather_data = [get_weather(city) for city in cities[:5]]  # Отримуємо погоду для перших 5 міст

    return render(request, 'weatherapp/all.html', {'weather_data': weather_data})


class WeatherAPIView(APIView):
    """
    API-клас для отримання погоди через REST API.
    """

    def get(self, request, city):
        """
        Отримує погоду для вказаного міста у форматі JSON.

        :param request: HTTP-запит
        :param city: Назва міста
        :return: JSON-об'єкт з погодними даними або повідомлення про помилку
        """
        weather = get_weather(city)
        if weather['description'] == 'City not found':
            return Response({"error": "City not found"}, status=404)

        weather['icon'] = f"http://openweathermap.org/img/w/{weather['icon']}.png"
        return Response(weather)
