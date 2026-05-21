from celery import shared_task
from apps.amp.models.maintenance_task import MaintenanceTask
from apps.amp.services.due_calculation_service import DueCalculationService
from apps.aircraft.models.aircraft import Aircraft
import logging

logger = logging.getLogger(__name__)


@shared_task
def recalculate_all_tasks():

    tasks = MaintenanceTask.objects.select_related("aircraft").all()

    for task in tasks:
        aircraft = task.aircraft

        status = DueCalculationService.calculate_task_status(task, aircraft)
        logger.info(
            f"Recalculated task {task.title} for aircraft {aircraft.tail_number}: {status}")
        print(f"{task.title} -----------> {status}")
