from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import DriverProfile
from .serializers import DriverProfileSerializer


# Create your views here.
class DriverProfileViewSet(ModelViewSet):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer
