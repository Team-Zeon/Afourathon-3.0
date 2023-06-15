from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.mixins import ListModelMixin
from .models import User
from .serializers import UserSerializer
from .permissions import FullDjangoModelPermissions


# Create your views here.
class CreateUserViewSets(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [FullDjangoModelPermissions]
