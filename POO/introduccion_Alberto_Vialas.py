import math
import random
import string

class Persona:
    #Constructor de la clase Persona que inicializa los atributos de la persona
    def __init__(self, nombre, edad, sexo, dni, peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.comprobarSexo()
        self.peso = peso
        self.altura = altura

    #Método que devuelve True si la persona es mayor de edad (tiene más de 18 años)
    def esMayorDeEdad(self): 
        if(int(self.edad)>18):
            return True
    
    #Método que comprueba el sexo introducido, y si no es válido, lo modifica
    def comprobarSexo(self):
        exit=False
        while(exit!=True):
            if(self.sexo!="M" and self.sexo!="H"):
                print("Por favor, indique un género válido (M, H)")
                self.sexo=input()
            else: 
                exit=True
        
    #Método que calcula el índice de masa corporal (IMC) de la persona         
    def calculaIMC(self):
        imc=float(self.peso)/(math.pow(float(self.altura), 2))
        return imc

class Password:
    #Constructor de la clase Password que inicializa la longitud de la contraseña y genera una contraseña aleatoria
    def __init__(self, longitud):
        self.longitud = longitud
        self.password = self.generarPassword()

    #Método que genera una contraseña aleatoria con la longitud especificada
    def generarPassword(self):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for i in range(self.longitud))

    #Método que comprueba si la contraseña es fuerte
    def esFuerte(self):
        num_mayusculas = sum(1 for c in self.password if c.isupper())
        num_minusculas = sum(1 for c in self.password if c.islower())
        num_numeros = sum(1 for c in self.password if c.isdigit())
        return num_mayusculas >= 2 and num_minusculas >= 1 and num_numeros >= 5

#Ejemplos de uso de las clases Persona y Password
Paula = Persona("Paula", 21, "M", "00000000A", 60, 1.60)
Alberto= Persona("Alberto", 22, "H", "11111111P")
print(Paula.calculaIMC())  #Imprime el IMC de Paula
print(Alberto.esMayorDeEdad())  #Imprime si Alberto es mayor de edad
print(Paula.esMayorDeEdad())  #Imprime si Paula es mayor de edad
password = Password(10)  #Crea una contraseña con longitud 10
print(password.password)  #Imprime la contraseña generada
print(password.esFuerte())  #Imprime si la contraseña es fuerte o no