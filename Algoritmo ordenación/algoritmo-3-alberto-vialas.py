#Creamos una sencilla función para introducir datos a nuestro array
def introducedatos(array):
    for i in range(10):
        nuevodato = input("por favor, introduzca un nuevo valor para introducir en el array: ")
        array.append(int(nuevodato))
    return array

#Creamos la función para ordenar el array
def ordenarray(array):
    if(len(array)>1):
        centro=len(array)//2
        arrayi = array[:centro]
        arrayd = array[centro:]

        #Llamada recursiva para ordenar las mitades
        ordenarray(arrayi)
        ordenarray(arrayd)

        #Combinación de las mitades ordenadas, vamos comparando ambos array guiados por indices, y los vamos almacenando en el array final.
        indicei = 0
        indiced = 0
        inicefinal = 0
        while indicei < len(arrayi) and indiced < len(arrayd):
            if arrayi[indicei] < arrayd[indiced]:
                array[inicefinal] = arrayi[indicei]
                indicei += 1
            else:
                array[inicefinal] = arrayd[indiced]
                indiced += 1
            inicefinal += 1

        while indicei < len(arrayi):
            array[inicefinal] = arrayi[indicei]
            indicei += 1
            inicefinal += 1

        while indiced < len(arrayd):
            array[inicefinal] = arrayd[indiced]
            indiced += 1
            inicefinal += 1
    return array

#Inicio del programa
nuevoarray = []
introducedatos(nuevoarray)
print(ordenarray(nuevoarray))