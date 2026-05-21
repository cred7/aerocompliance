from celery import shared_task
from apps.ad.services.scheduling_service import ADSchedulingService


@shared_task
def run_ad_compliance_check():
    ADSchedulingService.update_all_statuses()
    return "AD compliance recalculated"
