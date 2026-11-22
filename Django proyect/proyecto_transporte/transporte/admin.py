from django.contrib import admin
from .models import Ruta, Parada, Conductor, Unidad

admin.site.register(Ruta)
admin.site.register(Parada)
admin.site.register(Conductor)
admin.site.register(Unidad)