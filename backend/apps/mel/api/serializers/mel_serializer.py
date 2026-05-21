from rest_framework import serializers
from apps.mel.models.mel_item import MELItem


class MELSerializer(serializers.ModelSerializer):

    class Meta:
        model = MELItem
        fields = "__all__"
