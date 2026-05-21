from rest_framework.views import APIView
from rest_framework.response import Response

from apps.dashboards.services.fleet_dashboard_service import FleetDashboardService
from apps.dashboards.services.aircraft_dashboard_service import AircraftDashboardService


class FleetDashboardView(APIView):

    def get(self, request):

        data = FleetDashboardService.get_fleet_overview()
        return Response(data)


class AircraftDashboardView(APIView):

    def get(self, request, aircraft_id):

        data = AircraftDashboardService.get_aircraft_status(aircraft_id)
        return Response(data)
