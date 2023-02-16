#Recorremos el array deseado, y si encontramos el valor, devolvemos True, si no, False
def busqueda(vector, valor):
    for i in range(len(vector)):
        if(vector[i]==valor):
            return True
    return False

#Creamos un array e iniciamos el programa
nuevoarray=[1, 8, 5, 3, 0, 75]
exit=False
while(exit != True):
    buscado=input("qué valor desea buscar? (exit para salir): ")
    if(buscado=="exit"):
        exit=True
    else:
        if(busqueda(nuevoarray, int(buscado))):
            print("El valor existe")
        else:
            print("el valor no existe")