from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    """Overriding the default Django User model to add more fields
    Args:
        AbstractUser (_type_): _description_
    """

    role = models.CharField(max_length=50, null=True)
    password = models.CharField(_("password"), max_length=128, null=True)
