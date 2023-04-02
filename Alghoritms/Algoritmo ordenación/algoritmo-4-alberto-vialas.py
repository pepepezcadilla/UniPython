#Comprobamos si la lista está ordenada, definimos el puntero, iniciamos un bucle para ir ordenandolo y utilizamos recursividad para ir ordenandolo
def ordenar(lista):
    if len(lista) <= 1:
        return lista
    else:
        p = lista[-1]
        i = -1
        for j in range(len(lista)-1):
            if lista[j] <= p:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i+1], lista[-1] = lista[-1], lista[i+1]
        left = ordenar(lista[:i+1])
        right = ordenar(lista[i+2:])
        return left + [p] + right

#Inicio del programa
lista = [20, 8, 10, 9, 15]
print(ordenar(lista))