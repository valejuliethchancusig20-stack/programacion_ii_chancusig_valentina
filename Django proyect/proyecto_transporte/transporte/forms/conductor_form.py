from django import forms
from transporte.models import Conductor


class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ["cedula", "nombres", "apellidos", "licencia", "telefono", "activo"]