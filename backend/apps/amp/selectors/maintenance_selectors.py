from apps.amp.models.maintenance_task import MaintenanceTask


def get_aircraft_tasks(aircraft_id: int):
    return MaintenanceTask.objects.filter(aircraft_id=aircraft_id, is_active=True)
