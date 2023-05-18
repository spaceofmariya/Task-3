from django.urls import path
from registered import views


app_name = "registered"


urlpatterns = [
    path("submit/", views.register, name="submit"),
    #  path('delete/<int:id>/',views.delete, name="delete"),
    # path('edit/<int:id>/',views.edit, name="edit"),
]