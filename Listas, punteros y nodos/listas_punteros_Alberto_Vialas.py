#Se aconseja implementar, modificando lo que se considere necesario en función de cada opción,  al menos, las siguientes funciones:

#crear_nodo  hecho  hecho(diccionario)         función que crea la estructura de datos de un nodo y su contenido. Dicha estructura será tipo diccionario.
#insertar_inicio  hecho      función que añade un nuevo nodo al inicio de la lista. Si la lista está vacía, la crea con el valor correspondiente.
#insertar_nodo      hecho            # función que añade un nodo nuevo entre otros dos nodos ya existentes. Si fuera un nodo inicial o final, lo inserta en su correspondiente posición.
#insertar_final     hecho    función que añade un nodo al final de la lista. Si la lista está vacía, no podrá insertar ningún nodo.
#contar_nodos    hecho    función que devuelve el número de nodos de una lista
#eliminar_nodo   hecho    función que le pide al usuario un nodo y si está, se elimina de la lista.
#imprimir_valor_lista  hecho      función que imprime el valor de cada nodo (se deja como ampliación el modo en el que muestra la lista)
#imprimir_lista_completa  hecho  función que imprime todos los campos de cada nodo
#imprimir_reves   hecho   función que imprime la lista desde el final al principio (se deja como ampliación el modo en el que muestra la lista)
#buscar_nodo    hecho     función que busca un nodo dentro de la lista
#copiar_lista.           función que copia una lista (con todos sus campos) a un fichero llamado "lista_tipo.txt", de forma que "tipo" puede tomar los siguientes valores en función del tipo de lista que es:
#enlazada          en este caso el fichero se llamará "lista_enlazada.txt"
#enlazada_d      en este caso el fichero se llamará "lista_enlazada_d.txt"
#circular             en este caso el fichero se llamará "lista_circular.txt"
#circular_d.        en este caso el fichero se llamará "lista_circular_d.txt"


#Creamos el menú principal para elegir el tipo de lista
def menulistas():
    exit=False
    while(exit!=True):
        print("------------------------------------")
        print("---------Menú-----listas------------")
        print("------------------------------------")
        print("1- Listas enlazadas")
        print("2- Listas doblementre enlazadas")
        print("3- Listas circulares enlazadas")
        print("4- Listas circulares doblemente enlazadas")
        print("5- Exit")
        print("Introduzca la opción deseada")
        opcionmenu1 = int(input)

        if (opcionmenu1==1):
            listasenlazadas()
        elif(opcionmenu1==2):
            listadenlazadas()
        elif(opcionmenu1==3):
            listacenlazadas()
        elif(opcionmenu1==4):
            listacdenlazadas()
        elif(opcionmenu1==5):
            exit=True


def listasenlazadas():
    exit=False

    listaenlazada = []
    listaenlazada = crealistae(listaenlazada)
    while(exit!=True):
        print("------------------------------------")
        print("-------Menú-listas-enlazadas--------")
        print("------------------------------------")
        print("1-Crear nodo")
        print("2-Eliminar nodo")
        print("3-Contar nodos")
        print("4-Buscar nodo")
        print("5-Imprimir datos")
        print("6-Imprimir lista completa")
        print("7-Imprimir lista al revés")
        print("8-Copiar lista")
        print("9-Exit")
        print("Introduzca la opción deseada")
        opcionmenu2 = int(input)

        if (opcionmenu2==1):
            datos=input("Introduzca los datos del nuevo nodo")
            nodonuevo=crear_nodo(datos)
            print("Dónde desea introducir el nodo? (1-al principio, 2-en una posición exacta, 3-al final, 4-no deseo introducirlo")
            opcion=int(input)
            if(opcion==1):
                insertar_inicio(listaenlazada, nodonuevo)
            elif(opcion==2):
                posicion=int(input("Introduzca la posición deseada: "))
                insertar_nodo(listaenlazada, nodonuevo, posicion)
            elif(opcion==3):
                insertar_final(listaenlazada, nodonuevo)
        elif(opcionmenu2==2):
            nodoeliminado=int(input(""))
        elif(opcionmenu2==3):
            listacenlazadas()
        elif(opcionmenu2==4):
            listacdenlazadas()
        elif(opcionmenu2==5):
            exit=True
        elif(opcionmenu2==6):
            exit=True
        elif(opcionmenu2==7):
            exit=True
        elif(opcionmenu2==8):
            exit=True
        elif(opcionmenu2==9):
            exit=True


def crealistae(lista):
    nodo1= crear_nodo("0")
    nodo2= crear_nodo("1")
    nodo3= crear_nodo("2")
    nodo4= crear_nodo("3")
    nodo5= crear_nodo("4")
    nodo6= crear_nodo("5")

    nodo1.next = nodo2
    nodo2.next = nodo3
    nodo3.next = nodo4
    nodo4.next = nodo5
    nodo5.next = nodo6

    lista.append(nodo1)
    lista.append(nodo2)
    lista.append(nodo3)
    lista.append(nodo4)
    lista.append(nodo5)
    lista.append(nodo6)
    return lista























#Creamos el objeto nodo y le implementamos un constructor
class node:
    def __init__(self, datos):
        self.nodo = {"datos": datos, "next": None, "prev": None}
    
    def __getitem__(self, key):
        return self.nodo[key]

def crear_nodo(datos):
    nodocreado = node(datos)
    return nodocreado


def insertar_inicio(lista, nodo):
    lista.insert(0, nodo)
    return lista

def insertar_nodo(lista, nodo, posicion):
    if(posicion > len(lista)):
        lista.insert((len(lista)+1), nodo)
    else:
        lista.insert(posicion, nodo)
    return lista

def insertar_final(lista, nodo):
    lista.append(nodo)
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

def eliminar_nodo(lista, posicion):
    del lista[posicion]
    return lista

def imprimir_lista(lista):
    print(lista)
    return lista

def imprimir_lista_completa(lista):
    for i in range (len(lista)):
        print(lista[i]['datos'])


def imprimir_reves(lista):
    lista.reverse()
    for i in range (len(lista)):
        print(lista[i]['datos'])


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
listaenlazada=[]
nodonuevo = crear_nodo("pruebainicio")
listaenlazada = insertar_inicio(listaenlazada, nodonuevo)
listaenlazada = insertar_nodo(listaenlazada, nodonuevo, 50)
long=contar_nodo(listaenlazada)
print("La longitud es: "+str(long))
print(listaenlazada[0][key])

imprimir_lista(listaenlazada)
imprimir_lista_completa(listaenlazada)
imprimir_reves(listaenlazada)
