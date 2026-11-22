from django.urls import path
from transporte.views import parada_lista, parada_crear

urlpatterns = [
    path("", parada_lista, name="parada_lista"),
    path("nuevo/", parada_crear, name="parada_crear"),
]