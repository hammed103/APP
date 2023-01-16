from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import permissions


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # API Schema:
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    
]


admin.site.site_header = "Axxase Admin"
admin.site.site_title = "Axxase control panel"
admin.site.index_title = "Welcome to Axxase Admin"
