from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        QA = "QA", "QA"
        ENGINEER = "ENGINEER", "Engineer"
        CAMO = "CAMO", "CAMO Planner"

    role = models.CharField(max_length=20, choices=Role.choices)
    is_active_engineer = models.BooleanField(default=True)

    # User can be assigned to manage/maintain specific aircraft
    assigned_aircraft = models.ManyToManyField(
        "aircraft.Aircraft",
        related_name="assigned_users",
        blank=True,
        help_text="Aircraft this user is responsible for"
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
