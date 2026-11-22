from django.shortcuts import render, redirect
from transporte.models import Parada
from transporte.forms import ParadaForm


def parada_lista(request):
    paradas = Parada.objects.select_related("ruta").all()
    return render(request, "transporte/paradas/lista.html", {"paradas": paradas})


def parada_crear(request):
    if request.method == "POST":
        form = ParadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("parada_lista")
    else:
        form = ParadaForm()
    return render(request, "transporte/paradas/form.html", {"form": form, "titulo": "Nueva Parada"})