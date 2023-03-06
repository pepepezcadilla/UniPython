def primo(numero):
    #Verifica si un número es primo.
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def capicua(numero):
    #Verifica si un número es capicúa
    return str(numero) == str(numero)[::-1]

#Inicio del programa
contadort = 0
total_sum = 0
actual = 2

while contadort < 20:
    if primo(actual) and capicua(actual):
        contadort += 1
        total_sum += actual
        print(actual)
    actual += 1

print("La suma de los primeros 20 números primos capicúa es:"+str(total_sum))