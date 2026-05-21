from django.db import models
from apps.ad.models.airworthiness_directive import AirworthinessDirective
from apps.aircraft.models.aircraft import Aircraft


class ADCompliance(models.Model):

    class Status(models.TextChoices):
        COMPLIANT = "COMPLIANT", "Compliant"
        DUE = "DUE", "Due"
        OVERDUE = "OVERDUE", "Overdue"
        NOT_APPLICABLE = "NA", "Not Applicable"

    ad = models.ForeignKey(
        AirworthinessDirective,
        on_delete=models.CASCADE,
        related_name="compliances",
    )

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE,
        related_name="ad_compliances",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DUE,
    )

    last_compliance_fh = models.FloatField(default=0)
    last_compliance_fc = models.IntegerField(default=0)
    last_compliance_date = models.DateField(null=True, blank=True)

    next_due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
