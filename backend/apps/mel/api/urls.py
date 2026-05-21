from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.mel.api.views.mel_viewset import MELViewSet

router = DefaultRouter()
router.register(r"mel", MELViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
