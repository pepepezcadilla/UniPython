from datetime import date

#Creamos la clase Paciente e iniciamos sus atributos
class Paciente():
    def __init__(self, nombre, apellidos, dni, historial, ultfech):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.historial = historial
        self.ultfech = ultfech

    #Creamos el método __str__ para poder ver todos los atributos
    def __str__(self):
        return "{} {}, DNI: {}, nº Historial Clínico: {}, última fecha de ingreao: {}".format(self.nombre, self.apellidos, self.dni, self.historial, self.ultfech)
    
    #Creamos el método para ver sólo la última fecha de ingreso
    def ingreso(self):
        return "Último ingreso: {}".format(self.ultfech)
    
    #Calculamos cuántos días han pasado desde el último ingreso
    def dias(self):
        hoy = date.today()
        diferencia = hoy - self.ultfech
        num_dias = diferencia.days

        return num_dias
    
#Creamos un Paciente de prueba para mostrar el funcionamiento
fecha1= date(2021, 3, 6)
paciente1 = Paciente("Mariana", "Torres", "60367212K", 100357602, fecha1)
print(paciente1)
print(paciente1.ingreso())
print(paciente1.dias())