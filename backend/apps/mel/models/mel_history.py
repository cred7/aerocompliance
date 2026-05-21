from django.db import models
from django.conf import settings
from apps.mel.models.mel_item import MELItem


class MELHistory(models.Model):

    mel_item = models.ForeignKey(
        MELItem,
        on_delete=models.CASCADE,
        related_name="history",
    )

    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)

    note = models.TextField(blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
