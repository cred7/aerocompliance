from apps.ad.models.ad_compliance import ADCompliance


def get_aircraft_ad_compliance(aircraft_id: int):
    return ADCompliance.objects.filter(
        aircraft_id=aircraft_id
    ).select_related("ad")
