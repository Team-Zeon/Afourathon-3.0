from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"assignment", views.AssignmentViewSet)

urlpatterns = [
    # path("driver/", views.driver),
    # path("driver/<int:driver_id>/", views.driver),
    # path("car/", views.car),
    # path("car/<int:car_id>/", views.car),
    path("", include(router.urls)),
]
