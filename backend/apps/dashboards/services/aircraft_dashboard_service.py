from apps.aircraft.models.aircraft import Aircraft
from apps.mel.models.mel_item import MELItem
from apps.ad.models.ad_compliance import ADCompliance


class AircraftDashboardService:

    @staticmethod
    def get_aircraft_status(aircraft_id: int):

        aircraft = Aircraft.objects.get(id=aircraft_id)

        mel_items = MELItem.objects.filter(aircraft=aircraft)
        ad_items = ADCompliance.objects.filter(aircraft=aircraft)

        return {
            "aircraft": aircraft.tail_number,
            "total_mel": mel_items.count(),
            "open_mel": mel_items.filter(status="OPEN").count(),
            "expired_mel": mel_items.filter(status="EXPIRED").count(),
            "ad_compliant": ad_items.filter(status="COMPLIANT").count(),
            "ad_overdue": ad_items.filter(status="OVERDUE").count(),
        }
