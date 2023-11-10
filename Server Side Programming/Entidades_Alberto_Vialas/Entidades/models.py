from django.db import models

class Evento(models.Model):
    Nombre = models.CharField(max_length=255),
    Fecha = models.DateField(),
    Descripcion = models.TextField(),
    Duracion = models.FloatField(),
    Precio = models.FloatField(),
    Cliente = models.ManyToManyField('Cliente'),
    Ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE)

class Cliente(models.Model):
    Nombre = models.CharField(max_length=255),
    Apellido = models.CharField(max_length=255),
    Direccion = models.TextField(),
    Correo = models.CharField(max_length=255),
    Telefono = models.IntegerField(max_length=9),
    Asistencia = models.ManyToManyField(Evento),
    Entrada = models.OneToOneField('Entrada', on_delete=models.CASCADE)

class Entrada(models.Model):
    EntradaID = models.IntegerField(),
    Evento = models.ForeignKey('Evento', on_delete=models.CASCADE)

class Ubicacion(models.Model):
    Nombre = models.CharField(max_length=255),
    Direccion = models.TextField(),
    Aforo = models.IntegerField(),
    Equipamiento = models.TextField()

# Create your models here.
