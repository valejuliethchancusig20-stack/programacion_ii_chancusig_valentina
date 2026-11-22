from django import forms
from transporte.models import Ruta


class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ["codigo", "nombre", "origen", "destino", "tarifa", "activa"]