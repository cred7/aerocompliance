from rest_framework import serializers
from apps.ad.models.airworthiness_directive import AirworthinessDirective


class ADSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirworthinessDirective
        fields = "__all__"
