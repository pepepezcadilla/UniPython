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

#Creamos una función en la que, primero, dentro de un bucle while, comprobamos si nuestro array está ordenado. Luego, vamos comprobando posición por posición los elementos y los vamos ordenando poco a poco.
def ordenarray(array):
    acabado = False
    while(acabado!=True):
        acabado = compruebaorden(array)
        for i in range(9):
            if(array[i]>(array[i+1])):
                print(str(array[i])+" se ha cambiado por "+str(array[i+1]))
                array[i], array[i+1] = array[i+1], array[i]
    return array
                
#Inicio del programa
arrayuno = []
arrayuno=introducedatos(arrayuno)
arrayuno=ordenarray(arrayuno)
print(arrayuno)