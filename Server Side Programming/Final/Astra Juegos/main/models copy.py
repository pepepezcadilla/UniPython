from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.IntegerField()
    cantidad = models.PositiveIntegerField(default=10)


    class Meta:
        ordering = ['titulo']
        verbose_name_plural = "Videojuegos"

    def __str__(self) -> str:
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('videojuego', args=[str(self.id)])
    
class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    videojuego = models.ManyToManyField(Videojuego)


    class Meta:
        ordering = ['nombre']
        verbose_name_plural = "Plataformas"

    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('plataforma', args=[str(self.id)])

class Copia(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    alquilado = models.BooleanField()
    fecha_alquiler = models.DateField()
    fecha_limite = models.DateField()
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return str(self.pk) + ' '+ str(self.videojuego.titulo) 
    
class Consola(models.Model):
    nombre = models.CharField(max_length=100)