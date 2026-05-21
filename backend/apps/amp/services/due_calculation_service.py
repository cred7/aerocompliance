from datetime import date
from apps.amp.models.maintenance_task import MaintenanceTask
from apps.amp.models.compliance_status import ComplianceStatus


class DueCalculationService:

    @staticmethod
    def calculate_task_status(task: MaintenanceTask, aircraft):

        if task.interval_type == "FH":
            next_due = task.last_performed_fh + task.interval_value
            current = aircraft.total_flight_hours

            remaining = next_due - current

        elif task.interval_type == "FC":
            next_due = task.last_performed_fc + task.interval_value
            current = aircraft.total_flight_cycles

            remaining = next_due - current

        else:
            # CALENDAR
            if not task.last_performed_date:
                return ComplianceStatus.DUE

            delta = (date.today() - task.last_performed_date).days
            remaining = task.interval_value - delta

        if remaining <= 0:
            return ComplianceStatus.OVERDUE

        if remaining <= task.interval_value * 0.1:
            return ComplianceStatus.DUE

        return ComplianceStatus.COMPLIANT
