from django.db import models
from apps.amp.models.maintenance_task import MaintenanceTask
from django.conf import settings


class MaintenanceExecution(models.Model):

    task = models.ForeignKey(
        MaintenanceTask,
        on_delete=models.CASCADE,
        related_name="executions",
    )

    performed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    performed_fh = models.FloatField()
    performed_fc = models.IntegerField()
    performed_date = models.DateField()

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
