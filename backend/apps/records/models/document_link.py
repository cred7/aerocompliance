from django.db import models
from apps.records.models.document import Document
from apps.mel.models.mel_item import MELItem
from apps.amp.models.maintenance_task import MaintenanceTask
from apps.ad.models.airworthiness_directive import AirworthinessDirective


class DocumentLink(models.Model):

    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="links",
    )

    mel_item = models.ForeignKey(
        MELItem,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    maintenance_task = models.ForeignKey(
        MaintenanceTask,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    ad = models.ForeignKey(
        AirworthinessDirective,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
