from django.db import models
from car.models import CarProfile
from driver.models import DriverProfile


# Create your models here.
class Assignment(models.Model):
    car = models.OneToOneField(CarProfile, on_delete=models.CASCADE)
    driver = models.OneToOneField(DriverProfile, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
