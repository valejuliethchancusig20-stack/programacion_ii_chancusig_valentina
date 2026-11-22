from django.db import models


class Conductor(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    licencia = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.cedula})"