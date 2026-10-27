from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    raza = models.TextField(max_length=100)
    edad = models.TextField(blank=True)
    tamano = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

