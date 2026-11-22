from django.shortcuts import render
from transporte.models import Ruta, Parada, Conductor, Unidad


def inicio(request):
    contexto = {
        "total_rutas": Ruta.objects.count(),
        "total_paradas": Parada.objects.count(),
        "total_conductores": Conductor.objects.count(),
        "total_unidades": Unidad.objects.count(),
    }
    return render(request, "transporte/home.html", contexto)