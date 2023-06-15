from rest_framework import serializers
from .models import DriverProfile


class DriverProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()

    class Meta:
        model = DriverProfile
        fields = ["id", "name", "mail_id", "phone_number", "available", "user"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = instance.user.username
        return representation
