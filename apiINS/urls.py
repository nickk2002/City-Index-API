from django.urls import path

from apiINS import views

urlpatterns = [
    path("json/<str:matrix_code>/all", views.get_all, name='get_all'),
    path("json/<str:matrix_code>/<str:localitate>", views.get_location_json, name='get_localitate'),
    path("csv/<str:matrix_code>/<str:localitate>", views.get_location_csv, name='get_localitate')
]
