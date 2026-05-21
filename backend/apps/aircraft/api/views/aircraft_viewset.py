from django.apps import apps
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Prefetch

from apps.aircraft.models.aircraft import Aircraft
from apps.aircraft.api.serializers.aircraft_serializer import (
    AircraftSerializer,
    AircraftDetailSerializer,
    MELItemListSerializer,
    ADComplianceListSerializer,
    MaintenanceTaskListSerializer,
    ComplianceSnapshotListSerializer,
    DocumentListSerializer,
    AuditLogListSerializer,
)
from apps.aircraft.services.aircraft_service import AircraftService


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.select_related(
        "aircraft_type",
        "operator",
    )

    serializer_class = AircraftSerializer

    def get_queryset(self):
        """Optimize queryset based on action"""
        queryset = super().get_queryset()

        if self.action == 'retrieve' or self.action == 'aircraft_detail':
            # Heavy optimization for detail views
            queryset = queryset.prefetch_related(
                'mel_items',
                'ad_compliances',
                'maintenance_tasks',
                'documents',
                'audit_logs',
            )

        return queryset

    def get_serializer_class(self):
        """Use detail serializer for detail views"""
        if self.action == 'retrieve' or self.action == 'aircraft_detail':
            return AircraftDetailSerializer
        return AircraftSerializer

    def perform_create(self, serializer):
        AircraftService.create_aircraft(
            validated_data=serializer.validated_data,
            user=self.request.user,
        )

    def perform_update(self, serializer):
        AircraftService.update_aircraft(
            instance=self.get_object(),
            validated_data=serializer.validated_data,
            user=self.request.user,
        )

    def perform_destroy(self, instance):
        AircraftService.delete_aircraft(
            instance=instance,
            user=self.request.user,
        )

    @action(detail=True, methods=['get'])
    def aircraft_detail(self, request, pk=None):
        """
        Get comprehensive aircraft operational detail.

        Includes:
        - Basic aircraft info
        - All MEL items
        - All AD compliances
        - All AMP maintenance tasks
        - Compliance snapshot
        - Document records
        - Recent audit history
        - Operational statistics
        """
        aircraft = self.get_object()
        serializer = self.get_serializer(aircraft)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def mel_items(self, request, pk=None):
        """Get all MEL items for this aircraft"""
        aircraft = self.get_object()
        mel_items = aircraft.mel_items.all()
        serializer = MELItemListSerializer(mel_items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def ad_compliances(self, request, pk=None):
        """Get all AD compliances for this aircraft"""
        aircraft = self.get_object()
        ad_compliances = aircraft.ad_compliances.all()
        serializer = ADComplianceListSerializer(ad_compliances, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def maintenance_tasks(self, request, pk=None):
        """Get all maintenance tasks for this aircraft"""
        aircraft = self.get_object()
        tasks = aircraft.maintenance_tasks.all()
        serializer = MaintenanceTaskListSerializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def compliance_snapshot(self, request, pk=None):
        """Get compliance snapshot for this aircraft"""
        aircraft = self.get_object()
        snapshot = getattr(aircraft, 'compliance_snapshot', None)
        if snapshot:
            serializer = ComplianceSnapshotListSerializer(snapshot)
            return Response(serializer.data)
        return Response({"detail": "No compliance snapshot available"}, status=404)

    @action(detail=True, methods=['get'])
    def documents(self, request, pk=None):
        """Get all documents for this aircraft"""
        aircraft = self.get_object()
        documents = aircraft.documents.all().order_by('-uploaded_at')
        serializer = DocumentListSerializer(documents, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def audit_history(self, request, pk=None):
        """Get audit history for this aircraft (last 50 entries)"""
        aircraft = self.get_object()
        audit_logs = aircraft.audit_logs.all().order_by('-timestamp')[:50]
        serializer = AuditLogListSerializer(audit_logs, many=True)
        return Response(serializer.data)
