from django.urls import path

from apiCFR import views

urlpatterns = [
    path("", views.trains, name="standard_request")
]
