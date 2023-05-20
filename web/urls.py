from django.urls import path
from web import views


app_name = "web"


urlpatterns = [
    path("", views.index, name="index"),
    path("logged-in/", views.register, name="userPage"),
    path("participant-details/<int:id>/", views.details, name="details")
]