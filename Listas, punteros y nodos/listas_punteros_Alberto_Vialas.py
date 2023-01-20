#Creamos el diccionario que almacenará los nodos
listaenlazada = {}

#Creamos el objeto nodo y le implementamos un constructor
class Nodo:
    def constructor(self, datos):
        self.datos = datos
        self.next = None

def crear_nodo(datos):
    nodocreado = Nodo(datos)
    
