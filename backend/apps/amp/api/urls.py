from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.amp.api.views.maintenance_task_viewset import MaintenanceTaskViewSet

router = DefaultRouter()
router.register(r"tasks", MaintenanceTaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
