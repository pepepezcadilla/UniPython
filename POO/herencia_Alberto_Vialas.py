class Vehiculo():

    def __init__(self, color, ruedas, nombre):
        self.color = color
        self.ruedas = ruedas
        self.nombre = nombre

    def __str__(self):
        return "Color {}, {} ruedas. Modelo: {}".format(self.color, self.ruedas, self.nombre)
    
class Coche(Vehiculo):

    def __init__(self, color, ruedas, nombre, velocidad, cilindrada):
        super().__init__(color, ruedas, nombre)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)
    
class Limusina(Coche):
    def __init__(self, color, ruedas, nombre, velocidad, cilindrada, asientos, puertas):
        super().__init__(color, ruedas, nombre, velocidad, cilindrada)
        self.asientos = asientos
        self.puertas = puertas

    def __str__(self):
        return super().__str__() + ", {} asientos, {} puertas.".format(self.asientos, self.puertas)

class Tanque(Vehiculo):

    def __init__(self, color, ruedas, nombre, velocidad, cilindrada, ocupantes):
        super().__init__(color, ruedas, nombre)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.ocupantes = ocupantes

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc, {} ocupantes".format(self.velocidad, self.cilindrada, self.ocupantes)
    
class Camion(Tanque):
    def __init__(self, color, ruedas, nombre, velocidad, cilindrada, ocupantes, asientos, armas):
        super().__init__(color, ruedas, nombre, velocidad, cilindrada, ocupantes)
        self.asientos = asientos
        if isinstance(armas, bool):
            self.armas = armas
        else: 
            self.armas = False

    def __str__(self):
        return super().__str__() + ", {} asientos, {} armas.".format(self.asientos, self.armas)

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, nombre, tipo, peso):
        super().__init__(color, ruedas, nombre)
        self.tipo = tipo
        self.peso = peso

    def __str__(self):
        return super().__str__() + ", tipo {}, {} kg".format(self.tipo, self.peso)
    
class Triciclo(Bicicleta):
    def __init__(self, color, ruedas, nombre, velocidad, cilindrada, bocina):
        super().__init__(color, ruedas, nombre, velocidad, cilindrada)
        if isinstance(bocina, bool):
            self.bocina = bocina
        else: 
            self.bocina = False

    def __str__(self):
        return super().__str__() + ", {} bocina.".format(self.bocina)
    
lim = Limusina("negro", "4", "Limus3000", "120", "44", "15", "8")
print(lim)

cam = Camion("Camuflaje verde", 6, "Camion de Contrabando", 100, 30, 6, 5, True)
print(cam)

tri = Triciclo("Rojo", 3, "Trici30", "calle", "2.6", True)
print(tri)