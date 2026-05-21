from apps.aircraft.models.aircraft import Aircraft
from apps.compliance.models.compliance_snapshot import ComplianceSnapshot
from apps.mel.models.mel_item import MELItem


class FleetDashboardService:

    @staticmethod
    def get_fleet_overview():

        total_aircraft = Aircraft.objects.count()

        snapshots = ComplianceSnapshot.objects.select_related("aircraft")

        airworthy = snapshots.filter(overall_status="AIRWORTHY").count()
        restricted = snapshots.filter(overall_status="RESTRICTED").count()
        unfit = snapshots.filter(overall_status="UNFIT").count()

        mel_open = MELItem.objects.filter(status="OPEN").count()
        mel_overdue = MELItem.objects.filter(status="EXPIRED").count()

        return {
            "fleet_size": total_aircraft,
            "airworthy": airworthy,
            "restricted": restricted,
            "unfit": unfit,
            "mel_open": mel_open,
            "mel_overdue": mel_overdue,
        }
