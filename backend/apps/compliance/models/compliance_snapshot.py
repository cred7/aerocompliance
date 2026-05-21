from django.db import models
from apps.aircraft.models.aircraft import Aircraft


class ComplianceSnapshot(models.Model):

    class Status(models.TextChoices):
        AIRWORTHY = "AIRWORTHY", "Airworthy"
        RESTRICTED = "RESTRICTED", "Restricted"
        UNFIT = "UNFIT", "Unfit"

    aircraft = models.OneToOneField(
        Aircraft,
        on_delete=models.CASCADE,
        related_name="compliance_snapshot",
    )

    amp_status = models.CharField(max_length=20)
    mel_status = models.CharField(max_length=20)
    ad_status = models.CharField(max_length=20)

    overall_status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AIRWORTHY,
    )

    last_evaluated = models.DateTimeField(auto_now=True)
