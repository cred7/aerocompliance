from django.contrib import admin

# Register your models here.
from apps.compliance.models.compliance_snapshot import ComplianceSnapshot

admin.site.register(ComplianceSnapshot)
