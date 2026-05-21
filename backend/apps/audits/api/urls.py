from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.audits.api.views.audit_log_viewset import AuditLogViewSet

router = DefaultRouter()
router.register(r"logs", AuditLogViewSet, basename="audit-logs")

urlpatterns = [
    path("", include(router.urls)),
]
