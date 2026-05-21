from apps.dashboards.services.fleet_dashboard_service import FleetDashboardService


def get_fleet_dashboard_data():
    return FleetDashboardService.get_fleet_overview()
