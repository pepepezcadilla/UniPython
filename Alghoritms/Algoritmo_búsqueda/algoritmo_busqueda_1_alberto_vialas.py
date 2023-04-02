#Recorremos el array deseado, y si encontramos el valor, devolvemos True y la posición, si no, False
def busqueda(vector, valor):
    for i in range(len(vector)):
        if(vector[i]==valor):
            return True, i
    return False

#Creamos un array e iniciamos el programa
nuevoarray=[1, 8, 5, 3, 0, 75, 9, 2, 10, 800]
exit=False
while(exit != True):
    buscado=input("qué valor desea buscar? (exit para salir): ")
    if(buscado=="exit"):
        exit=True
    else:
        buscar, posicion=busqueda(nuevoarray, int(buscado))
        if(buscar):
            print("El valor existe, está en la posición "+str(posicion))
        else:
            print("el valor no existe")