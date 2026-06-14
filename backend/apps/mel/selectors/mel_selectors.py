from apps.mel.models.mel_item import MELItem


def get_aircraft_mel_items(aircraft_id: int):
    return MELItem.objects.filter(aircraft_id=aircraft_id).order_by("-created_at")


def get_open_mel_items():
    return MELItem.objects.filter(status="OPEN")
