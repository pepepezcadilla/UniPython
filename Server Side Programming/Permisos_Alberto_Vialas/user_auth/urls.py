# user_auth/urls.py

from django.urls import path
from .views import index, crear_pelicula, actoresypelis, crear_actor

urlpatterns = [
    path('', index, name='index'),
    path('crear_pelicula/', crear_pelicula, name='crear_pelicula'),
    path('actoresypelis/', actoresypelis, name='actoresypelis'),
     path('crear_actor/', crear_actor, name='crear_actor'),
]
