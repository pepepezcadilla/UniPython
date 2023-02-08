#Creamos una sencilla función para introducir datos a nuestro array
def introducedatos(array):
    for i in range(10):
        nuevodato = input("por favor, introduzca un nuevo valor para introducir en el array: ")
        array.append(int(nuevodato))
    return array

#Creamos una función para comprobar si nuestro array está ordenado, y devolvemos true o false dependiendo de si lo está o no.
def compruebaorden(array):
    ordenado = False
    for i in range(9):
        if(array[i]>(array[i+1])):
            ordenado = False
            return ordenado
        else:
            ordenado = True
    return ordenado

#Creamos una finción en la cual se va comparando el valor del array seleccionado (dado por la variable posición) con el siguiente, hasta que encuentra un valor más alto.
def ordenarray(array):
    for p in range(10):
        posicion=0
        for x in range(9):
            if(array[posicion]>array[x+1]):
                print("cambio "+str(array[posicion])+" por "+str(array[x+1]))
                array[posicion], array[x+1] = array[x+1], array[posicion]
                posicion = posicion+1
            else:
                posicion = posicion+1
    return array

#Inicio del programa
arrayuno = []
arrayuno=introducedatos(arrayuno)
arrayuno=ordenarray(arrayuno)
print(arrayuno)