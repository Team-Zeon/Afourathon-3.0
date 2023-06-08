from rest_framework import serializers
from .models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"

    # car = CarProfileSerializer()
    # driver = DriverProfileSerializer()
