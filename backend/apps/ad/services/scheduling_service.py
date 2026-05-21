from apps.ad.models.ad_compliance import ADCompliance


class ADSchedulingService:

    @staticmethod
    def update_all_statuses():

        compliances = ADCompliance.objects.select_related(
            "ad",
            "aircraft"
        )

        for item in compliances:
            item.status = item.status  # placeholder for future engine
            item.save()
