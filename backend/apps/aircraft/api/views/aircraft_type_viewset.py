from rest_framework import viewsets

from apps.aircraft.models.aircraft_type import AircraftType
from apps.aircraft.api.serializers.aircraft_type_serializer import (
    AircraftTypeSerializer,
)


class AircraftTypeViewSet(viewsets.ModelViewSet):
    queryset = AircraftType.objects.all()
    serializer_class = AircraftTypeSerializer
