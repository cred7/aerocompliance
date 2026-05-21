from rest_framework import serializers
from apps.amp.models.maintenance_task import MaintenanceTask


class MaintenanceTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceTask
        fields = "__all__"
