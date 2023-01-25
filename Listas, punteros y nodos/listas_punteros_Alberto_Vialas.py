#Se aconseja implementar, modificando lo que se considere necesario en función de cada opción,  al menos, las siguientes funciones:

#crear_nodo  hecho           función que crea la estructura de datos de un nodo y su contenido. Dicha estructura será tipo diccionario.
#insertar_inicio  hecho      función que añade un nuevo nodo al inicio de la lista. Si la lista está vacía, la crea con el valor correspondiente.
#insertar_nodo        
#insertar_final         función que añade un nodo al final de la lista. Si la lista está vacía, no podrá insertar ningún nodo.
#contar_nodos        función que devuelve el número de nodos de una lista
#eliminar_nodo       función que le pide al usuario un nodo y si está, se elimina de la lista.
#imprimir_valor_lista        función que imprime el valor de cada nodo (se deja como ampliación el modo en el que muestra la lista)
#imprimir_lista_completa    función que imprime todos los campos de cada nodo
#imprimir_reves      función que imprime la lista desde el final al principio (se deja como ampliación el modo en el que muestra la lista)
#buscar_nodo    hecho     función que busca un nodo dentro de la lista
#copiar_lista.           función que copia una lista (con todos sus campos) a un fichero llamado "lista_tipo.txt", de forma que "tipo" puede tomar los siguientes valores en función del tipo de lista que es:
#enlazada          en este caso el fichero se llamará "lista_enlazada.txt"
#enlazada_d      en este caso el fichero se llamará "lista_enlazada_d.txt"
#circular             en este caso el fichero se llamará "lista_circular.txt"
#circular_d.        en este caso el fichero se llamará "lista_circular_d.txt"

#Creamos el diccionario que almacenará los nodos


#Creamos el objeto nodo y le implementamos un constructor
class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.next = None
        self.prev = None

def crear_nodo(datos):
    nodocreado = Nodo(datos)
    return nodocreado
    
def insertar_inicio(lista, nodo):
    lista["pos1"] = lista["head"]
    nodo.next = lista["head"]
    lista["head"].prev = nodo
    lista["head"] = nodo
    return lista

def insertar_nodo(lista, nodo):
    keybuscada = buscar_nodo(lista, nodo)
    print("key en insertar_nodo2"+str(buscar_nodo(lista, nodo)))
    return lista

def buscar_nodo(lista, nodo_buscado):
    for key, value in lista.items():
        if value == nodo_buscado:
            print("llave es "+str(key))
            return key
    return None



#Inicio del programa
listaenlazada = {}
nodo1= crear_nodo("Prueba1")
nodo1.next = "Prueba2"
nodo2= crear_nodo("Prueba2")
nodo2.next = ("Prueba1")
listaenlazada["head"]=nodo1
listaenlazada["pos1"]=nodo2
listaenlazada = insertar_inicio(listaenlazada, nodo2)

insertar_nodo(listaenlazada, nodo1)

print(listaenlazada["head"].datos)
print(listaenlazada["pos1"].datos)