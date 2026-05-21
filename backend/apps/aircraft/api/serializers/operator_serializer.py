from rest_framework import serializers
from apps.aircraft.models.operator import Operator


class OperatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operator
        fields = "__all__"
