from django.contrib import admin

# Register your models here.
# from apps.amp.models.compliance_status import ComplianceStatus
from apps.amp.models.maintenance_execution import MaintenanceExecution
from apps.amp.models.maintenance_task import MaintenanceTask

# admin.site.register(ComplianceStatus)
admin.site.register(MaintenanceExecution)
admin.site.register(MaintenanceTask)
