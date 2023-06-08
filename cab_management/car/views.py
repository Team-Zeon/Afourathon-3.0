from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CarProfile
from .serializers import CarProfileSerializer


# Create your views here.
class CarProfileViewSet(ModelViewSet):
    queryset = CarProfile.objects.all()
    serializer_class = CarProfileSerializer
