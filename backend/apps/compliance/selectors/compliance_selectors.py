from apps.compliance.models.compliance_snapshot import ComplianceSnapshot


def get_fleet_compliance():
    return ComplianceSnapshot.objects.select_related("aircraft")


def get_unfit_aircraft():
    return ComplianceSnapshot.objects.filter(overall_status="UNFIT")
