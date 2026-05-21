from django.db import models
from django.conf import settings


class Notification(models.Model):

    class Type(models.TextChoices):
        AMP = "AMP", "AMP"
        MEL = "MEL", "MEL"
        AD = "AD", "AD"
        SYSTEM = "SYSTEM", "System"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        SENT = "SENT", "Sent"
        FAILED = "FAILED", "Failed"

    aircraft = models.ForeignKey(
        "aircraft.Aircraft",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications",
    )

    title = models.CharField(max_length=255)
    message = models.TextField()

    type = models.CharField(max_length=20, choices=Type.choices)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
