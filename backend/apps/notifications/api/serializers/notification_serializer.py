from rest_framework import serializers
from apps.notifications.models.notification import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = "__all__"
