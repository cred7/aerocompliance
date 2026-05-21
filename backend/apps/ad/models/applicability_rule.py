from django.db import models
from apps.ad.models.airworthiness_directive import AirworthinessDirective
from apps.aircraft.models.aircraft_type import AircraftType


class ADApplicabilityRule(models.Model):

    ad = models.ForeignKey(
        AirworthinessDirective,
        on_delete=models.CASCADE,
        related_name="rules",
    )

    aircraft_type = models.ForeignKey(
        AircraftType,
        on_delete=models.CASCADE,
        related_name="ad_rules",
    )

    is_applicable = models.BooleanField(default=True)
