from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web.urls", namespace="web")),
    path("user/", include("users.urls", namespace="users")),
    path("register/", include("registered.urls", namespace="registered"))
]
