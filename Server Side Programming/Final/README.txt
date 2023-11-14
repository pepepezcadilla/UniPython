cambiar la funcionalidad de copias para que elegir si son de videojuegos o de consolas,
que te permita crear muchas copias a la vez ya que de un mismo juego va a tener misma descripciones etc solo distinto id (igual esto con un autoincrement y con un bucle for se consigue)


Hacer un opciones de admin que solo vea el admin y el de inventario para añadir, eliminar, actualizar videojuegos y consolas

Que los videojuegos/consolas que tenemos se muestren pero si algun usuario añade todo el stock q nos queda a su carrito que ya no se muestre ese producto. Una opcion para cancelar esa compra y devolver del carrito al stock otra vez.

hacer un submenu dentro del favicon del usuario con todo lo relacionado con el log in/out y su info de usuario relacionada

crear un modal (esto que sale pero no es ningun html extra) vistoso para el inicio de sesion y para que el usuario se registre si no lo ha hecho, ya que no puede comprar sin estar registrado


modificar todo nuestro front al sistema de herencia de plantilla de django y lo mismo con las imagenes.

buscar como modificar o donde estan las template de usuarios de django para añadir algunos campos como direccion para simular la compra
Me ha dicho carmen que me haga un usuario y herede la propiedades de los usuarios de django y ahi ya podemos modificar los campos como queramos


VAMOS A CENTRARNOS SOLO EN TODO LO RELACIONADO CON VIDEOJUEGOS
----------------------------
Esto esta en proyecto_miguel
Indagar como podemos almacenar el iframe y las imagenes de cada videojuego/consola en sql


Hay que crear un modelo extra para las unidades de las consolas
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