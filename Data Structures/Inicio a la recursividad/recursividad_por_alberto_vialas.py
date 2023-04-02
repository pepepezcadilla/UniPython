#Definimos la función factorial, la cual se llama a si misma para conseguir el factorial de un número
def factorial (numero):
    if(numero==1):
        return 1
    else:
        return numero*factorial(numero-1)

#Definimos la función multiplicación, la cual se llama a si misma para multiplicar dos números
def multiplicacion(numero, numero2):
    if numero2 == 1:
        return numero
    else:
        return numero + multiplicacion(numero, numero2-1)

#Definimos la función MCD, la cual se llama a si misma para conseguir el máximo común divisor
def mcd(numero, numero2):
    if numero2 == 0:
        return numero
    else:
        return mcd(numero2, numero % numero2)

#Definimos la función exponente, la cual se llama a si misma para sacar el exponente dado de un número.
def exponente(base, exp):
    if exp== 0:
        return 1
    else:
        return base * exponente(base, exp-1)

#Definimos la función fibonacci, la cual se llama a si misma para conseguir la sucesión de fibonacci (x números)
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Definimos la función resta, la cual se llama a si misma para restar dos números
def resta(numero, numero2):
    if numero2 == 0:
        return numero
    else:
        return resta(numero-1, numero2-1)

#Definimos la función hanoi, la cual va moviendo aros, llamandose a si misma, hasta que todos los aros están en la posición final
def hanoi(aros, origen, destino, auxiliar):
    if aros == 1:
        print("Mover disco 1 de "+str(origen)+" a "+str(destino))
        return
    hanoi(aros-1, origen, auxiliar, destino)
    print("Mover disco "+str(aros)+" de "+str(origen)+" a "+str(destino))
    hanoi(aros-1, auxiliar, destino, origen)

#inicio del programa
exit = False
while(exit!=True):
    print("------------------------------------")
    print("---------Menú-recursividad----------")
    print("------------------------------------")
    print("\n1- Factorial")
    print("2- Multiplicación")
    print("3- MCD")
    print("4- Exponente")
    print("5- Fibonacci")
    print("6- Resta")
    print("7- Hanoi")
    print("8- Salir.")
    opcion=int(input("Por favor, introduzca el número del ejercicio que desee ver: "))

    if(opcion==1):
        fac=input("Introduzca el número del que desea obtener el factorial: ")
        print(factorial(int(fac)))
    elif(opcion==2):
        num1=input("Introduzca el primer número a multiplicar: ")
        num2=input("Introduzca el segundo número a multipliicar: ")
        print(multiplicacion(int(num1), int(num2)))
    elif(opcion==3):
        mcd1=input("Introduzca el primer número para sacar el máximo común divisor: ")
        mcd2=input("Introduzca el segundo número para sacar el máximo común divisor: ")
        print(mcd(int(mcd1), int(mcd2)))
    elif(opcion==4):
        bas=input("Introduzca la base: ")
        expon=input("Introduzca el exponente: ")
        print(exponente(int(bas), int(expon)))
    elif(opcion==5):
        #Creamos un for y una lista para obtener sólo los x primeros números de la sucesión de fibonacci
        rango=input("Introduzca los números de la sucesión de fibonacci que desea ver (se recomienda que no sea un número muy alto): ")
        fib = []
        for i in range(int(rango)):
            fib.append(fibonacci(i))
        print(fib)
    elif(opcion==6):
        res1=input("Introduzca el primer número a restar: ")
        res2=input("Introduzca el segundo número a restar: ")
        print(resta(int(res1), int(res2)))
    elif(opcion==7):
        aros = int(input("Ingrese la cantidad de aros: "))
        hanoi(int(aros), 'A', 'C', 'B')
    elif(opcion==8):
        exit=True
    else:
        print("Introduzca una opción correcta por favor")