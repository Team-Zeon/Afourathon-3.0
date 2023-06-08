from django.db import models


# Create your models here.
class CarProfile(models.Model):
    reg_no = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
