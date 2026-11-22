from django.urls import include, path
from transporte.views import inicio

urlpatterns = [
    path("", inicio, name="inicio"),
    path("rutas/", include("transporte.urls.ruta_urls")),
    path("paradas/", include("transporte.urls.parada_urls")),
    path("conductores/", include("transporte.urls.conductor_urls")),
    path("unidades/", include("transporte.urls.unidad_urls")),
]