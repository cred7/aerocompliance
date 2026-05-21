from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.aircraft.api.views.operator_viewset import OperatorViewSet
from apps.aircraft.api.views.aircraft_type_viewset import AircraftTypeViewSet
from apps.aircraft.api.views.aircraft_viewset import AircraftViewSet

router = DefaultRouter()

router.register(r"operators", OperatorViewSet)
router.register(r"aircraft-types", AircraftTypeViewSet)
router.register(r"aircraft", AircraftViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
