from rest_framework import viewsets

from apps.ad.models.airworthiness_directive import AirworthinessDirective
from apps.ad.api.serializers.ad_serializer import ADSerializer


class ADViewSet(viewsets.ModelViewSet):
    queryset = AirworthinessDirective.objects.all()
    serializer_class = ADSerializer
