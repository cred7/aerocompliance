from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.compliance.models.compliance_snapshot import ComplianceSnapshot
from apps.compliance.api.serializers.compliance_serializer import (
    ComplianceSnapshotSerializer,
)


class ComplianceViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ComplianceSnapshot.objects.select_related("aircraft").order_by(
        "-last_evaluated"
    )
    serializer_class = ComplianceSnapshotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter by aircraft or overall status if provided"""
        queryset = super().get_queryset()
        aircraft_id = self.request.query_params.get("aircraft_id")
        overall_status = self.request.query_params.get("overall_status")

        if aircraft_id:
            queryset = queryset.filter(aircraft_id=aircraft_id)
        if overall_status:
            queryset = queryset.filter(overall_status=overall_status)

        return queryset

    @action(detail=False, methods=["get"])
    def by_aircraft(self, request):
        """Get compliance snapshot for a specific aircraft"""
        aircraft_id = request.query_params.get("aircraft_id")
        if not aircraft_id:
            return Response({"error": "aircraft_id parameter required"}, status=400)

        snapshot = self.get_queryset().filter(aircraft_id=aircraft_id).first()
        if snapshot:
            serializer = self.get_serializer(snapshot)
            return Response(serializer.data)
        return Response({"detail": "No compliance snapshot found"}, status=404)

    @action(detail=False, methods=["get"])
    def unfit_aircraft(self, request):
        """Get all unfit aircraft with compliance snapshots"""
        unfit = self.get_queryset().filter(overall_status="UNFIT")
        serializer = self.get_serializer(unfit, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def restricted_aircraft(self, request):
        """Get all restricted aircraft with compliance snapshots"""
        restricted = self.get_queryset().filter(overall_status="RESTRICTED")
        serializer = self.get_serializer(restricted, many=True)
        return Response(serializer.data)
