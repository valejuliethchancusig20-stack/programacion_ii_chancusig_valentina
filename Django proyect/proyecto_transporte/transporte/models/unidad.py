from django.db import models
from django.db.models import CheckConstraint, Q
from .ruta import Ruta
from .conductor import Conductor


class Unidad(models.Model):
    ESTADOS = [
        ("OPERATIVO", "Operativo"),
        ("MANTENIMIENTO", "En Mantenimiento"),
        ("FUERA_SERVICIO", "Fuera de Servicio"),
    ]

    placa = models.CharField(max_length=10, unique=True)
    numero_disco = models.CharField(max_length=10, unique=True)
    capacidad = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default="OPERATIVO")
    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, related_name="unidades")
    conductor = models.OneToOneField(
        Conductor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="unidad",
    )

    class Meta:
        constraints = [
            CheckConstraint(condition=Q(capacidad__gt=0), name="capacidad_mayor_cero")
        ]

    def __str__(self):
        return f"Disco {self.numero_disco} - {self.placa}"