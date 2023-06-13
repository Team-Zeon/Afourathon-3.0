from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Overriding the default Django User model to add more fields"""

    pass
    # password = models.CharField(_("password"), max_length=128, null=True)
