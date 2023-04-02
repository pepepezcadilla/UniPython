print("Creando las tuplas y asignándole valores.\n...\n...\n...\n...")
tuplauno=[1, 2, 3, 4, 5]
print("Tupla uno: ")
print(*tuplauno)
tuplados=([1,2,3,4],1, 2, 3, 4)
print("Tupla dos: ")
print(*tuplados)

print("Longitud de la primera tupla: "+str(len(tuplauno)))
print("Longitud de la segunda tupla: "+str(len(tuplados)))

print("Ya que no se puede eliminar un objeto de dentro de una tupla, vamos a ayudarnos de una lista para hacer algo parecido:")
listaux=[]
print("Eliminemos el 1 de la primera tupla:")
for i in range(len(tuplauno)):
    if tuplauno[i]!=1:
        listaux.append(tuplauno[i])
tuplauno=tuple(listaux)

print("Veamos cómo ha quedado: ")
print(*tuplauno)

print("Ahora veamos cómo se pueden 'añadir' elementos a una tupla: ")
tuplados= tuplados+(5, 6, 7)

print("Veamos cómo ha quedado: ")
print(*tuplados)