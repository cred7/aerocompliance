from django.db import models


class AirworthinessDirective(models.Model):

    class ComplianceType(models.TextChoices):
        ONE_TIME = "ONE_TIME", "One Time"
        RECURRING = "RECURRING", "Recurring"

    ad_number = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    compliance_type = models.CharField(
        max_length=20,
        choices=ComplianceType.choices,
    )

    # interval logic (if recurring)
    interval_fh = models.FloatField(null=True, blank=True)
    interval_fc = models.IntegerField(null=True, blank=True)
    interval_days = models.IntegerField(null=True, blank=True)

    effective_date = models.DateField()
    mandatory = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
