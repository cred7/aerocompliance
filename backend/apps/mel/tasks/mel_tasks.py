from celery import shared_task
from apps.mel.services.escalation_service import MELEscalationService


@shared_task
def run_mel_escalation_check():
    count = MELEscalationService.check_expired_items()
    return f"{count} MEL items escalated"
