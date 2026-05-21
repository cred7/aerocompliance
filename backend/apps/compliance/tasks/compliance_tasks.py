from celery import shared_task
from apps.aircraft.models.aircraft import Aircraft
from apps.compliance.services.compliance_engine import ComplianceEngine


@shared_task
def run_compliance_evaluation():

    aircraft_list = Aircraft.objects.all()

    for aircraft in aircraft_list:
        ComplianceEngine.evaluate_aircraft(aircraft)

    return f"{aircraft_list.count()} aircraft evaluated"
