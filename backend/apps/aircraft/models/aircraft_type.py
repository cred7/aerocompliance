from django.db import models


class AircraftType(models.Model):
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine_type = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("manufacturer", "model")
        ordering = ["manufacturer", "model"]

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
