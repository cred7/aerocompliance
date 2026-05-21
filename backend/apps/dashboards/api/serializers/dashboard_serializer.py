from rest_framework import serializers


class FleetDashboardSerializer(serializers.Serializer):

    fleet_size = serializers.IntegerField()
    airworthy = serializers.IntegerField()
    restricted = serializers.IntegerField()
    unfit = serializers.IntegerField()
    mel_open = serializers.IntegerField()
    mel_overdue = serializers.IntegerField()
