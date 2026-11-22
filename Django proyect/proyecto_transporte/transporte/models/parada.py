from django.db import models
from django.db.models import UniqueConstraint
from .ruta import Ruta


class Parada(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    orden = models.PositiveIntegerField()
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name="paradas")

    class Meta:
        ordering = ["ruta", "orden"]
        constraints = [
            UniqueConstraint(fields=["ruta", "orden"], name="unique_orden_por_ruta")
        ]

    def __str__(self):
        return f"{self.nombre} (Ruta: {self.ruta.codigo})"