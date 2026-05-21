from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.ad.api.views.ad_viewset import ADViewSet
from apps.ad.api.views.ad_compliance_viewset import ADComplianceViewSet

router = DefaultRouter()
router.register(r"ads", ADViewSet)
router.register(r"compliances", ADComplianceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
