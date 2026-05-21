from django.contrib import admin

# Register your models here.
from apps.mel.models.mel_history import MELHistory
from apps.mel.models.mel_item import MELItem

admin.site.register(MELHistory)
admin.site.register(MELItem)
