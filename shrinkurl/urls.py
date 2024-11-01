from django.urls import path

from . import views

#endpoint for shrinkurl

urlpatterns = [
    path("api/", views.insert_or_retrieve_url),
]