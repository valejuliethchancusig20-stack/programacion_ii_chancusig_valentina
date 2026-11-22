from django.shortcuts import render, redirect
from transporte.models import Conductor
from transporte.forms import ConductorForm


def conductor_lista(request):
    conductores = Conductor.objects.all()
    return render(request, "transporte/conductores/lista.html", {"conductores": conductores})


def conductor_crear(request):
    if request.method == "POST":
        form = ConductorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("conductor_lista")
    else:
        form = ConductorForm()
    return render(request, "transporte/conductores/form.html", {"form": form, "titulo": "Nuevo Conductor"})