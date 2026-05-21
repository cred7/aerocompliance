from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.audits.selectors.audit_selectors import get_model_audits, get_user_audits
from apps.audits.models import AuditLog
from apps.audits.api.serializers.audit_log_serializer import (
    AuditLogSerializer,
)


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AuditLog.objects.select_related(
        'user', 'aircraft').order_by('-timestamp')
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter by aircraft, user, action, or model if provided"""
        queryset = super().get_queryset()
        aircraft_id = self.request.query_params.get('aircraft_id')
        user_id = self.request.query_params.get('user_id')
        action = self.request.query_params.get('action')
        model_name = self.request.query_params.get('model_name')

        if aircraft_id:
            queryset = queryset.filter(aircraft_id=aircraft_id)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if action:
            queryset = queryset.filter(action=action)
        if model_name:
            queryset = queryset.filter(model_name=model_name)

        return queryset

    @action(detail=False, methods=['get'])
    def by_aircraft(self, request):
        """Get audit history for a specific aircraft"""
        aircraft_id = request.query_params.get('aircraft_id')
        if not aircraft_id:
            return Response({"error": "aircraft_id parameter required"}, status=400)

        logs = self.get_queryset().filter(aircraft_id=aircraft_id)
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get audit history for a specific user"""
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id parameter required"}, status=400)

        logs = self.get_queryset().filter(user_id=user_id)
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_model(self, request):
        """Get audit history for a specific model"""
        model_name = request.query_params.get('model_name')
        if not model_name:
            return Response({"error": "model_name parameter required"}, status=400)

        logs = self.get_queryset().filter(model_name=model_name)
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data)
