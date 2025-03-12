from django.db import models

class CityWeather(models.Model):
    city = models.CharField(max_length=100)
    temp = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.city} - {self.temp}°C'