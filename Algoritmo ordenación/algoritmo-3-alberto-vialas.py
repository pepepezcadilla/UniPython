#Creamos una sencilla función para introducir datos a nuestro array
def introducedatos(array):
    for i in range(10):
        nuevodato = input("por favor, introduzca un nuevo valor para introducir en el array: ")
        array.append(int(nuevodato))
    return array


def ordenarray(array):
    if(len(array)>1):
        centro=len(array)//2