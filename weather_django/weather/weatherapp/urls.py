from django.urls import path
from .views import WeatherAPIView
from . import views

urlpatterns = [
    path('', views.all_index, name='all_index'),
    path('search', views.index, name='index'),
    path('api/weather/<str:city>/', WeatherAPIView.as_view(), name='weather-api'),

]