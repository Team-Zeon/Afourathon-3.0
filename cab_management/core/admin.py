from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = [
        "id",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    ]
