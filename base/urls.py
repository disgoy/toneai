from django.urls import path

from . import views

urlpatterns = [
    # ex: /ironic/
    path("", views.index, name="index"),
]