from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.compliance.api.views.compliance_viewset import ComplianceViewSet

router = DefaultRouter()
router.register(r"snapshots", ComplianceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
