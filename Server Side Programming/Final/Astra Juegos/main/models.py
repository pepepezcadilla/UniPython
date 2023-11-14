from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Empresa(models.Model):
  
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    telefono = models.CharField(max_length=255, verbose_name='Teléfono')
    nif = models.CharField(max_length=255, verbose_name='NIF')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self) -> str:
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('empresa', args=[str(self.id)])


class Videojuego(models.Model):

    titulo = models.CharField(max_length=255, verbose_name='Título')
    genero = models.CharField(max_length=255, verbose_name='Género')
    plataforma = models.CharField(max_length=255, verbose_name='Plataforma')
    fecha_lanzamiento = models.DateField(verbose_name='Fecha de lanzamiento')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    imagen = models.ImageField(upload_to='videojuegos',default="juego.png")
    iframe_code = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'

    def __str__(self) -> str:
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('videojuego', args=[str(self.id)])


class Consola(models.Model):

    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    fabricante = models.CharField(max_length=255, verbose_name='Fabricante')
    fecha_lanzamiento = models.DateField(verbose_name='Fecha de lanzamiento')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    plataforma = models.CharField(max_length=255, verbose_name='Plataforma')

    class Meta:
        verbose_name = 'Consola'
        verbose_name_plural = 'Consolas'

    def __str__(self) -> str:
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('consola', args=[str(self.id)])


class Unidad_V(models.Model):

    numero_serie = models.AutoField(primary_key=True, verbose_name='Número de serie')
    fecha_compra = models.DateField(verbose_name='Fecha de compra')
    estado = models.CharField(
        max_length=255, 
        choices=(
            ('nuevo', 'Nuevo'),
            ('usado', 'Usado'),
            ('dañado', 'Dañado'),
            ('perdido', 'Perdido'),
        ),
        verbose_name='Estado',
        default='nuevo',
    )
  
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE, verbose_name='Videojuego')

    class Meta:
        verbose_name = 'Copia'
        verbose_name_plural = 'Copias'

    def __str__(self) -> str:
        return self.numero_serie + ' ' + self.videojuego.titulo
    
    def get_absolute_url(self):
        return reverse('copia', args=[str(self.id)])
    
class Unidad_C(models.Model):

    numero_serie = models.AutoField(primary_key=True, verbose_name='Número de serie')
    fecha_compra = models.DateField(verbose_name='Fecha de compra')
    estado = models.CharField(
        max_length=255, 
        choices=(
            ('nuevo', 'Nuevo'),
            ('usado', 'Usado'),
            ('dañado', 'Dañado'),
            ('perdido', 'Perdido'),
        ),
        verbose_name='Estado',
        default='nuevo',
    )

    consola = models.ForeignKey(Consola, on_delete=models.CASCADE, verbose_name='Consola')

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'

    def __str__(self) -> str:
        return self.numero_serie + ' ' + self.consola.nombre

    def get_absolute_url(self):
        return reverse('copia', args=[str(self.id)])
