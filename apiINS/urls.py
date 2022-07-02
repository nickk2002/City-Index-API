from django.urls import path

from apiINS import views

urlpatterns = [
    path("json/<str:matrix_code>/", views.get_location_json, name='get_localitate'),
]
