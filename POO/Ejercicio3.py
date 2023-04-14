import math

#Creamos la clase Triangulo e iniciamos sus atributos
class Triangulo():
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    #Creamos el metodo para leer sus atributos
    def __str__(self):
        return "Tiángulo de cuyos lados son de: {}, {}, {}.".format(self.lado1, self.lado2, self.lado3)

    #Creamos el metodo para modificar los lados
    def modificar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    #Creamos los métodos para saber qué lado es mayor y menor
    def ladomayor(self):
        return max(self.lado1, self.lado2, self.lado3)
        
    def ladomenor(self):
        return min(self.lado1, self.lado2, self.lado3)
    
    #Creamos el método para saber el área (fórmula de Herón)
    def area(self):
        s = (self.perimetro()) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area

    #Creamos el método para saber el perímetro
    def perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro
    
    #Creamos el métod para saber qué tipo de triangulo se ha proporcionado
    def tipotr(self):
        if(self.lado1 == self.lado2):
            if(self.lado1 ==self.lado3):
                return "equilatero"
            else:
                return "isósceles"
        if(self.lado2 == self.lado3):
            if(self.lado2 ==self.lado1):
                return "equilatero"
            else:
                return "isósceles"
        if(self.lado3 == self.lado2):
            if(self.lado3 ==self.lado1):
                return "equilatero"
            else:
                return "isósceles"
        return "escaleno"

#Creamos un triángulo, vemos sus atributos y lo modificamos dos veces para tener todos los tipos de triángulo.
triangulo =Triangulo(3, 3, 3)
print(triangulo)
print(triangulo.ladomayor())
print(triangulo.ladomenor())
print(triangulo.area())
print(triangulo.perimetro())
print(triangulo.tipotr())
triangulo.modificar(3, 3, 5)
print(triangulo)
print(triangulo.ladomayor())
print(triangulo.ladomenor())
print(triangulo.area())
print(triangulo.perimetro())
print(triangulo.tipotr())
triangulo.modificar(3, 6, 5)
print(triangulo)
print(triangulo.ladomayor())
print(triangulo.ladomenor())
print(triangulo.area())
print(triangulo.perimetro())
print(triangulo.tipotr())
        