from django.contrib import admin
from .models import Empresa, Videojuego, Consola, Copia
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Videojuego)
admin.site.register(Consola)
admin.site.register(Copia)
