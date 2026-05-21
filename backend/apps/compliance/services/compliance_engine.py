from apps.aircraft.models.aircraft import Aircraft

from apps.amp.services.due_calculation_service import DueCalculationService
from apps.mel.models.mel_item import MELItem
from apps.ad.services.compliance_service import ADComplianceService
from apps.compliance.models.compliance_snapshot import ComplianceSnapshot


class ComplianceEngine:

    @staticmethod
    def evaluate_aircraft(aircraft: Aircraft):

        # -------------------------
        # AMP STATUS
        # -------------------------
        amp_tasks = aircraft.maintenance_tasks.all()

        amp_status = "COMPLIANT"

        for task in amp_tasks:
            status = DueCalculationService.calculate_task_status(
                task, aircraft)
            if status == "OVERDUE":
                amp_status = "NON_COMPLIANT"
                break

        # -------------------------
        # MEL STATUS
        # -------------------------
        mel_items = aircraft.mel_items.all()

        mel_status = "COMPLIANT"

        if mel_items.filter(status="EXPIRED").exists():
            mel_status = "NON_COMPLIANT"

        if mel_items.filter(status="OPEN").exists():
            mel_status = "WARNING"

        # -------------------------
        # AD STATUS
        # -------------------------
        ad_status = "COMPLIANT"

        if aircraft.ad_compliances.filter(status="OVERDUE").exists():
            ad_status = "NON_COMPLIANT"

        # -------------------------
        # OVERALL STATUS
        # -------------------------
        if "NON_COMPLIANT" in [amp_status, mel_status, ad_status]:
            overall = "UNFIT"
        elif "WARNING" in [mel_status]:
            overall = "RESTRICTED"
        else:
            overall = "AIRWORTHY"

        snapshot, _ = ComplianceSnapshot.objects.update_or_create(
            aircraft=aircraft,
            defaults={
                "amp_status": amp_status,
                "mel_status": mel_status,
                "ad_status": ad_status,
                "overall_status": overall,
            }
        )

        return snapshot
