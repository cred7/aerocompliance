from apps.notifications.services.notification_service import NotificationService
from apps.mel.models.mel_item import MELItem
from apps.aircraft.models.aircraft import Aircraft
import logging

logger = logging.getLogger(__name__)


class AlertEngine:

    @staticmethod
    def run_mel_alerts():

        expiring = MELItem.objects.filter(
            status="OPEN",
            remaining_hours__lte=5
        )

        for item in expiring:
            NotificationService.create_notification(
                user=item.aircraft.operator_id,  # replace with real user relation later
                title="MEL Expiry Warning",
                message=f"{item.title} is expiring soon",
                type="MEL"
            )

    @staticmethod
    def run_amp_alerts():

        for aircraft in Aircraft.objects.all():
            if aircraft.total_flight_hours > 1000:
                logger.info(
                    f" creating AMP alert for {aircraft.tail_number} with {aircraft.total_flight_hours} flight hours")
                NotificationService.create_notification(
                    # user=user,
                    title="AMP Alert",
                    message=f"{aircraft.tail_number} approaching maintenance threshold",
                    type="AMP"
                )
                logger.info(
                    f" created AMP alert for {aircraft.tail_number} with {aircraft.total_flight_hours} flight hours")

    @staticmethod
    def run_ad_alerts():

        for aircraft in Aircraft.objects.all():
            if aircraft.ad_compliances.filter(status="OVERDUE").exists():
                NotificationService.create_notification(
                    user=None,
                    title="AD OVERDUE",
                    message=f"{aircraft.tail_number} has overdue AD compliance",
                    type="AD"
                )
