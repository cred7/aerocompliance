from django.urls import path

from apps.dashboards.api.views.dashboard_view import (
    FleetDashboardView,
    AircraftDashboardView,
)

urlpatterns = [
    path("fleet/", FleetDashboardView.as_view()),
    path("aircraft/<int:aircraft_id>/", AircraftDashboardView.as_view()),
]
