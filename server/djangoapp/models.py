from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    CAR_TYPES = [
        ('SUV', 'SUV'),
        ('SEDAN', 'Sedan'),
        ('HYBRID', 'Hybrid'),
        ('EV', 'EV'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(min_value=2015, max_value=2023)

    def __str__(self):
        return self.name

