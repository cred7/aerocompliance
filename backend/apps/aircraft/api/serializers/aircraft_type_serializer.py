from rest_framework import serializers
from apps.aircraft.models.aircraft_type import AircraftType


class AircraftTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AircraftType
        fields = "__all__"
