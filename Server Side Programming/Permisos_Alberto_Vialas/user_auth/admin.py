from django.contrib import admin
from .models import UserProfile, Actor, Pelicula

admin.site.register(Actor)
admin.site.register(Pelicula)

admin.site.register(UserProfile)