from django.shortcuts import render, redirect
from transporte.models import Unidad
from transporte.forms import UnidadForm


def unidad_lista(request):
    unidades = Unidad.objects.select_related("ruta", "conductor").all()
    return render(request, "transporte/unidades/lista.html", {"unidades": unidades})


def unidad_crear(request):
    if request.method == "POST":
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("unidad_lista")
    else:
        form = UnidadForm()
    return render(request, "transporte/unidades/form.html", {"form": form, "titulo": "Nueva Unidad"})