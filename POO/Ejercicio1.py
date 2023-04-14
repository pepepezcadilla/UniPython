from datetime import date
from datetime import datetime

class Paciente():
    def __init__(self, nombre, apellidos, dni, historial, ultfech):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.historial = historial
        self.ultfech = ultfech

    def __str__(self):
        return "{} {}, DNI: {}, nº Historial Clínico: {}, última fecha de ingreao: {}".format(self.nombre, self.apellidos, self.dni, self.historial, self.ultfech)
    
    def ingreso(self):
        return "Último ingreso: {}".format(self.ultfech)
    
    def dias(self):
        hoy = datetime.date.today()
        diferencia = hoy - self.ultfech
        num_dias = diferencia.days

        return num_dias
    
