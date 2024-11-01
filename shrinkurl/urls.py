from django.urls import path

from . import views

urlpatterns = [
    path("shrinkurl/", views.insert_or_retrieve_url, name="shrinkurl"),
]