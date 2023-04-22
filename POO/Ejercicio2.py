from datetime import date

#Creamos la clase Alien e iniciamos sus atributos
class Alien():
    def __init__(self, nombre, patas, brazos, ojos, nacimiento):
        self.nombre = nombre
        self.patas = patas
        self.brazos = brazos
        self.ojos = ojos
        self.nacimiento = nacimiento

     #Creamos el método __str__ para poder ver todos los atributos
    def __str__(self):
        return "{}, {} patas, {} brazos, {} ojos. Nacido el {}".format(self.nombre, self.patas, self.brazos, self.ojos, self.nacimiento)

    #Calculamos cuántos años han pasado desde su nacimiento hasta hoy
    def esmayor(self):
        hoy = date.today()
        diferencia = hoy - self.nacimiento
        anios = int(diferencia.days / 365.25)  # 365.25 para tener en cuenta los años bisiestos
        if(anios>18):
            return True
        else :
            return False

#Creamos dos aliens de prueba
fecha1 = date(1903, 9, 15)
alien1 = Alien("Xenomprpho", 2, 2, 0, fecha1)
print(alien1)
print(alien1.esmayor())
fecha2 = date(2020, 12, 30)
alien2 = Alien("BMA", 4, 2, 8, fecha2)
print(alien2)
print(alien2.esmayor())