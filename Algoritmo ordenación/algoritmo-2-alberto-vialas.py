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

def ordenarray(array):
    acabado = False
    posicion = 0
    while(acabado!=True):
        acabado = compruebaorden(array)
        posicion = 0
        for x in range(10):
            for i in range(10):
                if(array[posicion]>array[i]):
                    array[posicion], array[i] = array[i], array[posicion]
                    posicion = i
                    print(array)
                else:
                    break
            print(array)
            posicion = x+1
    return array


arrayuno = []
arrayuno=introducedatos(arrayuno)
arrayuno=ordenarray(arrayuno)
print(arrayuno)