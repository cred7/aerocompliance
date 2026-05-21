from celery import shared_task
from apps.notifications.services.alert_engine import AlertEngine


@shared_task
def run_notification_engine():

    AlertEngine.run_mel_alerts()
    AlertEngine.run_amp_alerts()
    AlertEngine.run_ad_alerts()

    return f"Notification engine executed"
