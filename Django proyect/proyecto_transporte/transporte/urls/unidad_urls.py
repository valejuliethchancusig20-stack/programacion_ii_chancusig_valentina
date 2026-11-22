from django.urls import path
from transporte.views import unidad_lista, unidad_crear

urlpatterns = [
    path("", unidad_lista, name="unidad_lista"),
    path("nuevo/", unidad_crear, name="unidad_crear"),
]