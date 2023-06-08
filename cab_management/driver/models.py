from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class DriverProfile(models.Model):
    name = models.CharField(max_length=255)
    mail_id = models.EmailField(max_length=255)
    phone_number = PhoneNumberField()
    available = models.BooleanField(default=True)
