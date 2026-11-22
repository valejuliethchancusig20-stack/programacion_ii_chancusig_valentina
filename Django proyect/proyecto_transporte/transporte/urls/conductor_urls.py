from django.urls import path
from transporte.views import conductor_lista, conductor_crear

urlpatterns = [
    path("", conductor_lista, name="conductor_lista"),
    path("nuevo/", conductor_crear, name="conductor_crear"),
]