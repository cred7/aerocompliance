from django.db import models

from apps.aircraft.models.aircraft_type import AircraftType
from apps.aircraft.models.operator import Operator


class Aircraft(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        MAINTENANCE = "MAINTENANCE", "Maintenance"
        AOG = "AOG", "Aircraft On Ground"
        RETIRED = "RETIRED", "Retired"

    tail_number = models.CharField(max_length=20, unique=True)
    serial_number = models.CharField(max_length=100, unique=True)

    aircraft_type = models.ForeignKey(
        AircraftType,
        on_delete=models.PROTECT,
        related_name="aircraft",
    )

    operator = models.ForeignKey(
        Operator,
        on_delete=models.PROTECT,
        related_name="aircraft",
    )

    manufacture_date = models.DateField()

    total_flight_hours = models.FloatField(default=0)
    total_flight_cycles = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["tail_number"]
        indexes = [
            models.Index(fields=["tail_number"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return self.tail_number
