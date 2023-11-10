# user_auth/models.py

from django.db import models

class UserProfile(models.Model):
    nombre = models.CharField(max_length=255)
    passw = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10)


class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    año = models.IntegerField()

    def __str__(self):
        return self.titulo

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    peliculas = models.ManyToManyField('Pelicula')

    def __str__(self):
        return self.nombre
    