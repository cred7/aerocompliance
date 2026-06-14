from django.db import models
from django.conf import settings
from apps.aircraft.models.aircraft import Aircraft


class Document(models.Model):

    class Type(models.TextChoices):
        CRS = "CRS", "Certificate of Release to Service"
        WORK_ORDER = "WORK_ORDER", "Work Order"
        INSPECTION = "INSPECTION", "Inspection Report"
        AD_EVIDENCE = "AD_EVIDENCE", "AD Compliance Evidence"
        MEL_EVIDENCE = "MEL_EVIDENCE", "MEL Evidence"
        AMP_EVIDENCE = "AMP_EVIDENCE", "AMP Evidence"

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    type = models.CharField(max_length=30, choices=Type.choices)

    file = models.FileField(upload_to="aircraft_documents/", null=True, blank=True)

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)
