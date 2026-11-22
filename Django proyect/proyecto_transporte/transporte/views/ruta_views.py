from django.shortcuts import render, redirect
from django.db.models import Q
from transporte.models import Ruta
from transporte.forms import RutaForm


def ruta_lista(request):
    q = request.GET.get("q", "").strip()
    rutas = Ruta.objects.prefetch_related("paradas", "unidades")
    if q:
        rutas = rutas.filter(
            Q(codigo__icontains=q)
            | Q(nombre__icontains=q)
            | Q(origen__icontains=q)
            | Q(destino__icontains=q)
        )
    return render(request, "transporte/rutas/lista.html", {"rutas": rutas, "q": q})


def ruta_crear(request):
    if request.method == "POST":
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ruta_lista")
    else:
        form = RutaForm()
    return render(request, "transporte/rutas/form.html", {"form": form, "titulo": "Nueva Ruta"})