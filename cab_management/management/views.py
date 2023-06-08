from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from car.models import CarProfile
from driver.models import DriverProfile
from .models import Assignment
from .serializers import AssignmentSerializer


# Create your views here.
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def create(self, request, *args, **kwargs):
        car_id = request.data.get("car")
        driver_id = request.data.get("driver")

        if car_id and driver_id:
            car = get_object_or_404(CarProfile, pk=car_id)
            driver = get_object_or_404(DriverProfile, pk=driver_id)
            if not driver.available:
                return Response(
                    {"error": "The driver is not available for assignment."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not car.available:
                return Response(
                    {"error": "The car is not available for assignment."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            assignment = Assignment(car=car, driver=driver)
            assignment.save()
            car.available = False
            car.save()
            driver.available = False
            driver.save()
            serializer = AssignmentSerializer(assignment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if car_id:
            car = get_object_or_404(CarProfile, pk=car_id)
            if not car.available:
                return Response(
                    {"error": "The car is not available for assignment."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            driver = DriverProfile.objects.filter(available=True).first()
            if driver:
                assignment = Assignment(car=car, driver=driver)
                assignment.save()
                car.available = False
                car.save()
                driver.available = False
                driver.save()
                serializer = AssignmentSerializer(assignment)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "No available drivers."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if driver_id:
            driver = get_object_or_404(DriverProfile, pk=driver_id)
            if not driver.available:
                return Response(
                    {"error": "The driver is not available for assignment."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            car = CarProfile.objects.filter(available=True).first()
            if car:
                assignment = Assignment(car=car, driver=driver)
                assignment.save()
                car.available = False
                car.save()
                driver.available = False
                driver.save()
                serializer = AssignmentSerializer(assignment)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "No available cars."}, status=status.HTTP_400_BAD_REQUEST
                )

        return Response(
            {"error": "Please provide either car_id or driver_id."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, *args, **kwargs):
        return Response(
            {"error": "Method not allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def partial_update(self, request, *args, **kwargs):
        return Response(
            {"error": "Method not allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def perform_destroy(self, instance):
        car = instance.car
        driver = instance.driver

        car.available = True
        car.save()
        driver.available = True
        driver.save()

        instance.delete()

    # @action(detail=True, methods=["delete"])
    # def delete_assignment(self, request, pk=None):
    #     assignment = self.get_object()
    #     car = assignment.car
    #     driver = assignment.driver

    #     car.available = True
    #     car.save()
    #     driver.available = True
    #     driver.save()

    #     self.perform_destroy(assignment)

    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # @action(detail=True, methods=["put"])
    # def update_assignment(self, request, pk=None):
    #     assignment = self.get_object()
    #     serializer = self.get_serializer(assignment, data=request.data)

    #     if serializer.is_valid():
    #         car = assignment.car
    #         driver = assignment.driver

    #         car.available = True
    #         car.save()
    #         driver.available = True
    #         driver.save()

    #         self.perform_update(serializer)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
