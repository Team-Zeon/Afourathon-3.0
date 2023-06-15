from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from core.permissions import FullDjangoModelPermissions
from .models import CarProfile
from .serializers import CarProfileSerializer


# Create your views here.
class CarProfileViewSet(ModelViewSet):
    queryset = CarProfile.objects.all()
    serializer_class = CarProfileSerializer
    permission_classes = [FullDjangoModelPermissions]
