#Creamos el menú principal para elegir el tipo de lista
def menulistas():
    exit=False

    #creamos el menú por el cual elegimos el tipo de lista
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
        opcionmenu1 = int(input())

        if (opcionmenu1==1):
            listasenlazadas()
        elif(opcionmenu1==2):
            listasdenlazadas()
        elif(opcionmenu1==3):
            listascenlazadas()
        elif(opcionmenu1==4):
            listascdenlazadas()
        elif(opcionmenu1==5):
            exit=True


#creamos el menú para las listas enlazadas, creamos la lista y asignamos cada opción a una función diferente
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
        opcionmenu2 = int(input("Introduzca la opción deseada: "))

        if (opcionmenu2==1):
            #damos a elegir en qué posición va a estar situado el nodo
            id=input("Por favor, introdcuzca el identificador del nodo: ")
            datos=input("Introduzca los datos del nuevo nodo: ")
            nodonuevo=crear_nodo(id, datos)
            print("Dónde desea introducir el nodo? (1-al principio, 2-en una posición exacta, 3-al final, 4-no deseo introducirlo")
            opcion=int(input())
            if(opcion==1):
                insertar_inicio(listaenlazada, nodonuevo)
            elif(opcion==2):
                posicion=int(input("Introduzca la posición deseada: "))
                insertar_nodo(listaenlazada, nodonuevo, posicion)
            elif(opcion==3):
                insertar_final(listaenlazada, nodonuevo)
        elif(opcionmenu2==2):
            nodoeliminado=input("Por favor, introduzca el nodo que desea eliminar: ")
            eliminar_nodo(listaenlazada, nodoeliminado)
        elif(opcionmenu2==3):
            len=contar_nodo(listaenlazada)
        elif(opcionmenu2==4):
            nodo=input("Por favor, introdcuzca el nodo que desea buscar: ")
            buscar_nodo(listaenlazada, nodo)
        elif(opcionmenu2==5):
            imprimir_lista(listaenlazada)
        elif(opcionmenu2==6):
            imprimir_lista_completa(listaenlazada)
        elif(opcionmenu2==7):
            imprimir_reves(listaenlazada)
        elif(opcionmenu2==8):
            copiar_lista(listaenlazada, 1)
        elif(opcionmenu2==9):
            exit=True


#añadimos a la lista unos cuantos nodos
def crealistae(lista):
    nodo1= crear_nodo("nodo1", "1")
    nodo2= crear_nodo("nodo2", "2")
    nodo3= crear_nodo("nodo3", "3")
    nodo4= crear_nodo("nodo4", "4")
    nodo5= crear_nodo("nodo5", "5")
    nodo6= crear_nodo("nodo6", "6")

    nodo1["next"] = nodo2
    nodo2["next"] = nodo3
    nodo3["next"] = nodo4
    nodo4["next"] = nodo5
    nodo5["next"] = nodo6

    lista.append(nodo1)
    lista.append(nodo2)
    lista.append(nodo3)
    lista.append(nodo4)
    lista.append(nodo5)
    lista.append(nodo6)
    return lista


#creamos el menú para las listas doblemente enlazadas, creamos la lista y asignamos cada opción a una función diferente
def listasdenlazadas():
    exit=False

    listadenlazada = []
    listadenlazada = crealistade(listadenlazada)
    while(exit!=True):
        print("------------------------------------")
        print("--Menú-listas-doblemente-enlazadas--")
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
        opcionmenu2 = int(input("Introduzca la opción deseada: "))

        if (opcionmenu2==1):
            #damos a elegir en qué posición va a estar situado el nodo
            id=input("Por favor, introdcuzca el identificador del nodo: ")
            datos=input("Introduzca los datos del nuevo nodo: ")
            nodonuevo=crear_nodo(id, datos)
            print("Dónde desea introducir el nodo? (1-al principio, 2-en una posición exacta, 3-al final, 4-no deseo introducirlo")
            opcion=int(input())
            if(opcion==1):
                insertar_inicio(listadenlazada, nodonuevo)
            elif(opcion==2):
                posicion=int(input("Introduzca la posición deseada: "))
                insertar_nodo(listadenlazada, nodonuevo, posicion)
            elif(opcion==3):
                insertar_final(listadenlazada, nodonuevo)
        elif(opcionmenu2==2):
            nodoeliminado=input("Por favor, introduzca el nodo que desea eliminar: ")
            eliminar_nodo(listadenlazada, nodoeliminado)
        elif(opcionmenu2==3):
            len=contar_nodo(listadenlazada)
        elif(opcionmenu2==4):
            nodo=input("Por favor, introdcuzca el nodo que desea buscar: ")
            buscar_nodo(listadenlazada, nodo)
        elif(opcionmenu2==5):
            imprimir_lista(listadenlazada)
        elif(opcionmenu2==6):
            imprimir_lista_completa(listadenlazada)
        elif(opcionmenu2==7):
            imprimir_reves(listadenlazada)
        elif(opcionmenu2==8):
            copiar_lista(listadenlazada, 2)
        elif(opcionmenu2==9):
            exit=True


#añadimos a la lista unos cuantos nodos
def crealistade(lista):
    nodo1= crear_nodo("nodo1", "1")
    nodo2= crear_nodo("nodo2", "2")
    nodo3= crear_nodo("nodo3", "3")
    nodo4= crear_nodo("nodo4", "4")
    nodo5= crear_nodo("nodo5", "5")
    nodo6= crear_nodo("nodo6", "6")

    nodo1["next"] = nodo2
    nodo2["next"] = nodo3
    nodo2["prev"] = nodo1
    nodo3["next"] = nodo4
    nodo3["prev"] = nodo2
    nodo4["next"] = nodo5
    nodo4["prev"] = nodo3
    nodo5["next"] = nodo6
    nodo5["prev"] = nodo4
    nodo6["prev"] = nodo5

    lista.append(nodo1)
    lista.append(nodo2)
    lista.append(nodo3)
    lista.append(nodo4)
    lista.append(nodo5)
    lista.append(nodo6)
    return lista


#creamos el menú para las listas circulares, creamos la lista y asignamos cada opción a una función diferente
def listascenlazadas():
    exit=False

    listacenlazada = []
    listacenlazada = crealistac(listacenlazada)
    while(exit!=True):
        print("------------------------------------")
        print("-------Menú-listas-circulares-------")
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
        opcionmenu2 = int(input("Introduzca la opción deseada: "))

        if (opcionmenu2==1):
            #damos a elegir en qué posición va a estar situado el nodo
            id=input("Por favor, introdcuzca el identificador del nodo: ")
            datos=input("Introduzca los datos del nuevo nodo: ")
            nodonuevo=crear_nodo(id, datos)
            print("Dónde desea introducir el nodo? (1-al principio, 2-en una posición exacta, 3-al final, 4-no deseo introducirlo")
            opcion=int(input())
            if(opcion==1):
                insertar_inicio(listacenlazada, nodonuevo)
            elif(opcion==2):
                posicion=int(input("Introduzca la posición deseada: "))
                insertar_nodo(listacenlazada, nodonuevo, posicion)
            elif(opcion==3):
                insertar_final(listacenlazada, nodonuevo)
        elif(opcionmenu2==2):
            nodoeliminado=input("Por favor, introduzca el nodo que desea eliminar: ")
            eliminar_nodo(listacenlazada, nodoeliminado)
        elif(opcionmenu2==3):
            len=contar_nodo(listacenlazada)
        elif(opcionmenu2==4):
            nodo=input("Por favor, introdcuzca el nodo que desea buscar: ")
            buscar_nodo(listacenlazada, nodo)
        elif(opcionmenu2==5):
            imprimir_lista(listacenlazada)
        elif(opcionmenu2==6):
            imprimir_lista_completa(listacenlazada)
        elif(opcionmenu2==7):
            imprimir_reves(listacenlazada)
        elif(opcionmenu2==8):
            copiar_lista(listacenlazada, 3)
        elif(opcionmenu2==9):
            exit=True


#añadimos a la lista unos cuantos nodos
def crealistac(lista):
    nodo1= crear_nodo("nodo1", "1")
    nodo2= crear_nodo("nodo2", "2")
    nodo3= crear_nodo("nodo3", "3")
    nodo4= crear_nodo("nodo4", "4")
    nodo5= crear_nodo("nodo5", "5")
    nodo6= crear_nodo("nodo6", "6")

    nodo1["next"] = nodo2
    nodo2["next"] = nodo3
    nodo3["next"] = nodo4
    nodo4["next"] = nodo5
    nodo5["next"] = nodo6
    nodo6["next"] = nodo1

    lista.append(nodo1)
    lista.append(nodo2)
    lista.append(nodo3)
    lista.append(nodo4)
    lista.append(nodo5)
    lista.append(nodo6)
    return lista


#creamos el menú para las listas dovlemente circulares, creamos la lista y asignamos cada opción a una función diferente
def listascdenlazadas():
    exit=False

    listacdenlazada = []
    listacdenlazada = crealistacde(listacdenlazada)
    while(exit!=True):
        print("------------------------------------")
        print("--Menú-listas-doblemente-circulares-")
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
        opcionmenu2 = int(input("Introduzca la opción deseada: "))

        if (opcionmenu2==1):
            #damos a elegir en qué posición va a estar situado el nodo
            id=input("Por favor, introdcuzca el identificador del nodo: ")
            datos=input("Introduzca los datos del nuevo nodo: ")
            nodonuevo=crear_nodo(id, datos)
            print("Dónde desea introducir el nodo? (1-al principio, 2-en una posición exacta, 3-al final, 4-no deseo introducirlo")
            opcion=int(input())
            if(opcion==1):
                insertar_inicio(listacdenlazada, nodonuevo)
            elif(opcion==2):
                posicion=int(input("Introduzca la posición deseada: "))
                insertar_nodo(listacdenlazada, nodonuevo, posicion)
            elif(opcion==3):
                insertar_final(listacdenlazada, nodonuevo)
        elif(opcionmenu2==2):
            nodoeliminado=input("Por favor, introduzca el nodo que desea eliminar: ")
            eliminar_nodo(listacdenlazada, nodoeliminado)
        elif(opcionmenu2==3):
            len=contar_nodo(listacdenlazada)
        elif(opcionmenu2==4):
            nodo=input("Por favor, introdcuzca el nodo que desea buscar: ")
            buscar_nodo(listacdenlazada, nodo)
        elif(opcionmenu2==5):
            imprimir_lista(listacdenlazada)
        elif(opcionmenu2==6):
            imprimir_lista_completa(listacdenlazada)
        elif(opcionmenu2==7):
            imprimir_reves(listacdenlazada)
        elif(opcionmenu2==8):
            copiar_lista(listacdenlazada, 4)
        elif(opcionmenu2==9):
            exit=True


#añadimos a la lista unos cuantos nodos
def crealistacde(lista):
    nodo1= crear_nodo("nodo1", "1")
    nodo2= crear_nodo("nodo2", "2")
    nodo3= crear_nodo("nodo3", "3")
    nodo4= crear_nodo("nodo4", "4")
    nodo5= crear_nodo("nodo5", "5")
    nodo6= crear_nodo("nodo6", "6")

    nodo1["next"] = nodo2
    nodo1["prev"] = nodo6
    nodo2["next"] = nodo3
    nodo2["prev"] = nodo1
    nodo3["next"] = nodo4
    nodo3["prev"] = nodo2
    nodo4["next"] = nodo5
    nodo4["prev"] = nodo3
    nodo5["next"] = nodo6
    nodo5["prev"] = nodo4
    nodo6["next"] = nodo1
    nodo6["prev"] = nodo5

    lista.append(nodo1)
    lista.append(nodo2)
    lista.append(nodo3)
    lista.append(nodo4)
    lista.append(nodo5)
    lista.append(nodo6)
    return lista


#función para crear un nodo de clase diccionario
def crear_nodo(identificador, datos):
    nodocreado = {"id": identificador, "datos": datos, "next": None, "prev": None}
    return nodocreado


#insertamos un nodo en la posición 0 (el inicio)
def insertar_inicio(lista, nodo):
    lista.insert(0, nodo)
    return lista

#insertamos un nodo en la posición indicada, si es superior a la longitud de la lista, se añade al final
def insertar_nodo(lista, nodo, posicion):
    if(posicion > len(lista)):
        lista.insert((len(lista)+1), nodo)
    else:
        lista.insert(posicion, nodo)
    return lista

#insertamos un nodo al final de la lista
def insertar_final(lista, nodo):
    lista.append(nodo)
    return lista

#buscamos y mostramos un nodo, recorriendo toda la lista hasta encontrarlo
def buscar_nodo(lista, nodo_buscado):
    for elemento in lista:
        for key, values in elemento.items():
            if key == "id":
                if values == nodo_buscado:
                    print("Los datos del nodo "+str(values)+" son "+elemento["datos"])
    return None

#devolvemos la longitud de la lista
def contar_nodo(lista):
    longitud=len(lista)
    return longitud

#si el nodo seleccioando existe, lo eliminamos, recorriendo toda la lista hasta encontrarlo.
def eliminar_nodo(lista, borra):
    for elemento in lista:
        for key, values in elemento.items():
            if key == "id":
                if values == borra:
                    lista.remove(elemento)
                    
    return lista

#imprimimos los datos de todos los nodos
def imprimir_lista(lista):
    for i in range (len(lista)):
        print(lista[i]['datos'])

#imprimimos los identificadores y los datos de los nodos
def imprimir_lista_completa(lista):
    for i in range (len(lista)):
        print(lista[i]['id'],lista[i]['datos'])

#imprimimos los identificadores y los datos de los nodos, pero ordenados al revés
def imprimir_reves(lista):
    lista.reverse()
    for i in range (len(lista)):
        print(lista[i]['id'],lista[i]['datos'])

#copiamos el contenido de la lista suministrada al fichero de texto correspondiente, diferenciando entre los diferentes tipos de listas
def copiar_lista(lista, opcion):
    if(opcion==1):
        with open("lista_enlazada.txt", "w") as fichero:
            for i in range (len(lista)):
                fichero.write(lista[i]['id'],lista[i]['datos'])
            fichero.close
    elif(opcion==2):
        with open("lista_enlazada_d.txt", "w") as fichero:
            for i in range (len(lista)):
                fichero.write(lista[i]['id'],lista[i]['datos'])
            fichero.close
    elif(opcion==3):
        with open("lista_circular.txt", "w") as fichero:
            for i in range (len(lista)):
                fichero.write(lista[i]['id'],lista[i]['datos'])
            fichero.close
    elif(opcion==4):
        with open("lista_circular_d.txt", "w") as fichero:
            for i in range (len(lista)):
                fichero.write(lista[i]['id'],lista[i]['datos'])
            fichero.close

    
#Inicio del programa
menulistas()