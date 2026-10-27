from django.contrib import admin
from .models import Project, Animal


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Animal)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("raza", "fecha", "edad", "tamano")
    search_fields = ("edad", "raza")
