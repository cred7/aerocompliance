from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.ad.models.ad_compliance import ADCompliance
from apps.ad.api.serializers.ad_compliance_serializer import ADComplianceSerializer
from rest_framework.permissions import IsAuthenticated


class ADComplianceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for AD compliance status per aircraft.

    Supports filtering by:
    - aircraft_id: Filter compliances for specific aircraft
    - status: Filter by compliance status (COMPLIANT, DUE, OVERDUE, NA)
    """

    queryset = ADCompliance.objects.select_related("ad", "aircraft").order_by(
        "-updated_at"
    )
    serializer_class = ADComplianceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter by aircraft and status if provided"""
        queryset = super().get_queryset()
        aircraft_id = self.request.query_params.get("aircraft_id")
        status = self.request.query_params.get("status")

        if aircraft_id:
            queryset = queryset.filter(aircraft_id=aircraft_id)
        if status:
            queryset = queryset.filter(status=status)

        return queryset

    @action(detail=False, methods=["get"])
    def by_aircraft(self, request):
        """Get AD compliances for a specific aircraft"""
        aircraft_id = request.query_params.get("aircraft_id")
        if not aircraft_id:
            return Response({"error": "aircraft_id parameter required"}, status=400)

        compliances = self.get_queryset().filter(aircraft_id=aircraft_id)
        serializer = self.get_serializer(compliances, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def overdue(self, request):
        """Get all overdue AD compliances"""
        overdue = self.get_queryset().filter(status="OVERDUE")
        serializer = self.get_serializer(overdue, many=True)
        return Response(serializer.data)
