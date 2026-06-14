from apps.mel.models.mel_item import MELItem


class MELEscalationService:

    @staticmethod
    def check_expired_items():

        expired = MELItem.objects.filter(
            status__in=["OPEN", "IN_PROGRESS"], remaining_hours__lte=0
        )

        for item in expired:
            item.status = "EXPIRED"
            item.save()

        return expired.count()
