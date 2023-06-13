from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import DriverProfile
from .serializers import DriverProfileSerializer


# Create your views here.
class DriverProfileViewSet(ModelViewSet):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer

    def list(self, request, *args, **kwargs):
        print("...............")
        print(request.user)  # Print the request.user object
        return super().list(request, *args, **kwargs)
