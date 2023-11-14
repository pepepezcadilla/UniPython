from django.contrib import admin
from .models import Empresa, Videojuego, Consola, Unidad_C, Unidad_V
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Videojuego)
admin.site.register(Consola)
admin.site.register(Unidad_C)
admin.site.register(Unidad_V)

