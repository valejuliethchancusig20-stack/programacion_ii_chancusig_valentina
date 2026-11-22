from django.urls import path
from transporte.views import ruta_lista, ruta_crear

urlpatterns = [
    path("", ruta_lista, name="ruta_lista"),
    path("nueva/", ruta_crear, name="ruta_crear"),
]