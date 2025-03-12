from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime

def get_weather(city):
    #оримуємо дані погоди
    API_KEY = '' # ваш апі з openweathermap
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
    city = request.POST.get('city', 'Lviv')  # Отримуємо місто або 'Lviv' за замовчуванням
    weather = get_weather(city)
    return render(request, 'weatherapp/index.html', weather)


def all_index(request):
    cities = ['Lviv', 'Kyiv', 'Odessa', 'London', 'Dnipro']
    user_city = request.POST.get('city')

    if user_city and user_city not in cities:
        cities.insert(0, user_city)

    weather_data = [get_weather(city) for city in cities[:5]]  # Використовуємо функцію get_weather()

    return render(request, 'weatherapp/all.html', {'weather_data': weather_data})


class WeatherAPIView(APIView):
    def get(self, request, city):
        weather = get_weather(city)
        if weather['description'] == 'City not found':
            return Response({"error": "City not found"}, status=404)

        weather['icon'] = f"http://openweathermap.org/img/w/{weather['icon']}.png"
        return Response(weather)
