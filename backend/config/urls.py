"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/users/", include("apps.users.api.urls")),
    path("api/amp/", include("apps.amp.api.urls")),
    path("api/aircraft/", include("apps.aircraft.api.urls")),
    path("api/mel/", include("apps.mel.api.urls")),
    path("api/ad/", include("apps.ad.api.urls")),
    path("api/compliance/", include("apps.compliance.api.urls")),
    path("api/notifications/", include("apps.notifications.api.urls")),
    path("api/records/", include("apps.records.api.urls")),
    path("api/dashboard/", include("apps.dashboards.api.urls")),
    path("api/audits/", include("apps.audits.api.urls")),
]
