from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from apps.amp.models.maintenance_task import MaintenanceTask
from apps.amp.api.serializers.maintenance_task_serializer import MaintenanceTaskSerializer
from apps.audits.services.audit_service import AuditService
import logging
from apps.amp.services.due_calculation_service import DueCalculationService

logger = logging.getLogger(__name__)


class MaintenanceTaskViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceTask.objects.select_related(
        'aircraft').order_by('-created_at')
    serializer_class = MaintenanceTaskSerializer

    def get_queryset(self):
        """Filter by aircraft if provided"""
        queryset = super().get_queryset()
        aircraft_id = self.request.query_params.get('aircraft_id')
        is_active = self.request.query_params.get('is_active')

        if aircraft_id:
            queryset = queryset.filter(aircraft_id=aircraft_id)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        AuditService.log_create(
            user=request.user,
            instance=instance,
            after=serializer.data
        )

        logger.info(
            f"Maintenance task created ID={instance.pk} user={getattr(request.user, 'id', None)}"
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        before_data = self.get_serializer(instance).data

        response = super().update(request, *args, **kwargs)

        AuditService.log_update(
            user=request.user,
            instance=instance,
            before_data=before_data,
            after=response.data
        )

        logger.info(
            f"Maintenance task updated ID={instance.pk} user={getattr(request.user, 'id', None)}"
        )

        return response

    @action(detail=True, methods=['get'])
    def recalculate_status(self, request, pk=None):
        task = self.get_object()
        aircraft = task.aircraft

        status_result = DueCalculationService.calculate_task_status(
            task, aircraft)

        return Response({"status": status_result})

    @action(detail=False, methods=['get'])
    def by_aircraft(self, request):
        """Get maintenance tasks for a specific aircraft"""
        aircraft_id = request.query_params.get('aircraft_id')
        if not aircraft_id:
            return Response({"error": "aircraft_id parameter required"}, status=400)

        tasks = self.get_queryset().filter(aircraft_id=aircraft_id)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all active maintenance tasks"""
        tasks = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
