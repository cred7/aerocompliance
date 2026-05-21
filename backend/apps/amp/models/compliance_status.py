from django.db import models


class ComplianceStatus(models.TextChoices):
    COMPLIANT = "COMPLIANT", "Compliant"
    DUE = "DUE", "Due Soon"
    OVERDUE = "OVERDUE", "Overdue"
