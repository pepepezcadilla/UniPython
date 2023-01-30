#Se aconseja implementar, modificando lo que se considere necesario en función de cada opción,  al menos, las siguientes funciones:

#crear_nodo  hecho  hecho(diccionario)         función que crea la estructura de datos de un nodo y su contenido. Dicha estructura será tipo diccionario.
#insertar_inicio  hecho      función que añade un nuevo nodo al inicio de la lista. Si la lista está vacía, la crea con el valor correspondiente.
#insertar_nodo                  # función que añade un nodo nuevo entre otros dos nodos ya existentes. Si fuera un nodo inicial o final, lo inserta en su correspondiente posición.
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



#Creamos el objeto nodo y le implementamos un constructor
class Nodo:
    def __init__(self, datos):
        self.nodo = {"datos": datos, "next": None, "prev": None}
    
    def __getitem__(self, key):
        return self.nodo[key]

def crear_nodo(datos):
    nodocreado = Nodo(datos)
    return nodocreado
    
def insertar_inicio(lista, nodo):
    lista.insert(0, nodo)
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

def contar_nodo(lista):
    longitud=len(lista)
    return longitud



def crealista(lista):
    nodo1= crear_nodo("Prueba1")
    nodo2= crear_nodo("Prueba2")
    nodo3= crear_nodo("Prueba2")
    nodo4= crear_nodo("Prueba4")
    nodo5= crear_nodo("Prueba5")
    nodo6= crear_nodo("Prueba6")

    nodo1.next = nodo2
    nodo1.prev = nodo6
    nodo2.next = nodo3
    nodo2.prev = nodo1
    nodo3.next = nodo4
    nodo3.prev = nodo2
    nodo4.next = nodo5
    nodo4.prev = nodo3
    nodo5.next = nodo6
    nodo5.prev = nodo4
    nodo6.next = nodo1
    nodo6.prev = nodo5

    lista.append(nodo1)
    lista.append(nodo2)
    lista.append(nodo3)
    lista.append(nodo4)
    lista.append(nodo5)
    lista.append(nodo6)
    return lista
    
#Inicio del programa
listaenlazada = []
listaenlazada = crealista(listaenlazada)

nodonuevo = crear_nodo("pruebainicio")
listaenlazada = insertar_inicio(listaenlazada, nodonuevo)
long=contar_nodo(listaenlazada)
print("La longitud es: "+str(long))

print(listaenlazada[0]["datos"])