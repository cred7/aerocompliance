from rest_framework import viewsets

from apps.aircraft.models.operator import Operator
from apps.aircraft.api.serializers.operator_serializer import OperatorSerializer


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
