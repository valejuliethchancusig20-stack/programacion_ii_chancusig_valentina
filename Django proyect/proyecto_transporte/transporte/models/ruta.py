from django.db import models
from django.db.models import CheckConstraint, Q


class Ruta(models.Model):
    codigo = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tarifa = models.DecimalField(max_digits=5, decimal_places=2, default=0.35)
    activa = models.BooleanField(default=True)

    class Meta:
        constraints = [
            CheckConstraint(condition=Q(tarifa__gte=0), name="tarifa_no_negativa")
        ]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"