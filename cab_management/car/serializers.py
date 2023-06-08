from rest_framework import serializers
from .models import CarProfile


class CarProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarProfile
        fields = "__all__"
