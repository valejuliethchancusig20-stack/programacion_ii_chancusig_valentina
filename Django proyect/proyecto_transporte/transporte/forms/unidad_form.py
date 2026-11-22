from django import forms
from transporte.models import Unidad


class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ["placa", "numero_disco", "capacidad", "estado", "ruta", "conductor"]