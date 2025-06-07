from django.contrib import admin
from django.urls import path, include

# from rest_framework.schemas import get_schema_view
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("workdesk/", include("workdesk.urls")),
    path("project/", include("project.urls")),
    path("task/", include("task.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
