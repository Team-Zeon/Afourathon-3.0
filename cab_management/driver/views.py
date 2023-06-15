from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from core.permissions import FullDjangoModelPermissions
from .models import DriverProfile
from .serializers import DriverProfileSerializer


# Create your views here.
class DriverProfileViewSet(
    ListModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet
):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer
    permission_classes = [FullDjangoModelPermissions, IsAdminUser]

    @action(
        detail=False,
        methods=["get", "post"],
        permission_classes=[FullDjangoModelPermissions],
    )
    def me(self, request):
        if request.user.role != "driver":
            return Response({"detail": "You are not a driver"}, status=403)
        if request.method == "POST":
            user = get_user_model().objects.get(id=request.user.id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == "GET":
            driver = get_object_or_404(DriverProfile, user=request.user)
            serializer = self.get_serializer(driver)
            return Response(serializer.data)
