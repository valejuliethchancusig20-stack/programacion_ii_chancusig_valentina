from django import forms
from transporte.models import Parada


class ParadaForm(forms.ModelForm):
    class Meta:
        model = Parada
        fields = ["nombre", "direccion", "orden", "ruta"]