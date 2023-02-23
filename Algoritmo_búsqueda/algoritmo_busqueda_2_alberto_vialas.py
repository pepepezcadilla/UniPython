#Utilizamos un método iterativo para dividir la lista e ir buscando.
def buscariterativo(lista, valor):
    inicio = 0
    fin = len(lista) - 1
    medio = (inicio + fin) // 2
    while inicio <= fin:
        if lista[medio] == valor:
            return True
        elif lista[medio] > valor:
            fin = medio - 1
        else:
            inicio = medio + 1
        medio = (inicio + fin) // 2
    return False

#Utilizamos un método recursivo para dividir la lista e ir buscando.
def buscarecursivo(lista, valor, inicio, fin):
    if inicio > fin:
        return False
    medio = (inicio + fin) // 2
    if lista[medio] == valor:
        return True
    elif lista[medio] > valor:
        return buscarecursivo(lista, valor, inicio, medio - 1)
    else:
        return buscarecursivo(lista, valor, medio + 1, fin)

#Inicio del programa
exit=False
listabusqueda = [1, 3, 5, 7, 9, 11, 13, 15]
while(exit!=True):
    print("Qué método de bísqueda desea?:")
    print("1-Iterativo")
    print("2-Recursivo")
    print("3-Salir")
    opcion=int(input("Introduzca la opción deseada: "))
    if(opcion==1):
        busqueda=int(input("Qué número desea buscar?: "))
        if(buscariterativo(listabusqueda, busqueda)):
            print("El valor está en la lista")
        else:
            print("El valor no está en la lista.")
    elif(opcion==2):
        busqueda=int(input("Qué número desea buscar?: "))
        if(buscarecursivo(listabusqueda, busqueda, 0, len(listabusqueda) - 1)):
            print("El valor está en la lista")
        else:
            print("El valor no está en la lista.")
    elif(opcion==3):
        exit=True

        
