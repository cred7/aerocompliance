
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from apps.audits.services.audit_service import AuditService

from apps.notifications.models.notification import Notification
from apps.notifications.api.serializers.notification_serializer import NotificationSerializer
from apps.notifications.tasks.notification_tasks import run_notification_engine
from apps.amp.tasks.maintenance_tasks import recalculate_all_tasks


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Notification.objects.select_related(
        'aircraft', 'user').order_by("-created_at")
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter by aircraft, user, type, and status if provided"""
        queryset = super().get_queryset()
        aircraft_id = self.request.query_params.get('aircraft_id')
        notification_type = self.request.query_params.get('type')
        status = self.request.query_params.get('status')

        if aircraft_id:
            queryset = queryset.filter(aircraft_id=aircraft_id)
        if notification_type:
            queryset = queryset.filter(type=notification_type)
        if status:
            queryset = queryset.filter(status=status)

        return queryset

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def by_aircraft(self, request):
        """Get notifications for a specific aircraft"""
        aircraft_id = request.query_params.get('aircraft_id')
        if not aircraft_id:
            return Response({"error": "aircraft_id parameter required"}, status=400)

        notifications = self.get_queryset().filter(aircraft_id=aircraft_id)
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def pending(self, request):
        """Get all pending notifications"""
        pending = self.get_queryset().filter(status='PENDING')
        serializer = self.get_serializer(pending, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def run_engine(self, request):
        """Manually trigger notification engine"""
        run_notification_engine.delay()
        recalculate_all_tasks.delay()
        return Response({"status": "Notification engine executed"})
