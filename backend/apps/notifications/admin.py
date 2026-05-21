from django.contrib import admin

# Register your models here.
from apps.notifications.models.notification import Notification

admin.site.register(Notification)
