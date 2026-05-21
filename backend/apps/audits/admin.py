from django.contrib import admin

# Register your models here.
from apps.audits.models.audit_log import AuditLog

admin.site.register(AuditLog)
