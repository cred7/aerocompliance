from django.db import models
from apps.aircraft.models.aircraft import Aircraft


class MaintenanceTask(models.Model):

    class IntervalType(models.TextChoices):
        FLIGHT_HOURS = "FH", "Flight Hours"
        CYCLES = "FC", "Flight Cycles"
        CALENDAR = "CAL", "Calendar"

    title = models.CharField(
        max_length=255,
    )
    description = models.TextField(blank=True)

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE,
        related_name="maintenance_tasks",
    )

    interval_type = models.CharField(max_length=10, choices=IntervalType.choices)

    interval_value = models.FloatField()
    last_performed_fh = models.FloatField(default=0)
    last_performed_fc = models.IntegerField(default=0)
    last_performed_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
