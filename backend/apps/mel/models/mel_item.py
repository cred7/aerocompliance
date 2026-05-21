from django.db import models
from apps.aircraft.models.aircraft import Aircraft


class MELItem(models.Model):

    class Category(models.TextChoices):
        A = "A", "Category A"
        B = "B", "Category B"
        C = "C", "Category C"
        D = "D", "Category D"

    class Status(models.TextChoices):
        OPEN = "OPEN", "Open"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        CLOSED = "CLOSED", "Closed"
        EXPIRED = "EXPIRED", "Expired"

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE,
        related_name="mel_items",
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    category = models.CharField(max_length=1, choices=Category.choices)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )

    reported_date = models.DateTimeField(auto_now_add=True)

    # operational limits (in hours or days depending on config)
    allowed_duration_hours = models.FloatField()

    remaining_hours = models.FloatField()

    resolved_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
