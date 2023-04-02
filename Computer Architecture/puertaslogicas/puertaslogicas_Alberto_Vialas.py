import random

entrada=[]
intermedio=[]
salida=[]

#Los dos tienen que ser true para que devuelva true
def _and(x,y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0

#Si uno de los dos es true devuelve true
def _or(x,y):
    if x == 0 and y == 0:
        return 0
    else:
        return 1

#Devuelve true si la entrada es negativa
def _not(x):
    if x == 0:
        return 1
    else:
        return 0

#Da una salida falsa solo si todas sus entradas son verdaderas
def _nand(x,y):
    if x == 1 and y == 1:
        return 0
    else:
        return 1

#Es la negacion del operador OR
def _nor(x,y):
    if x == 0 and y == 0:
        return 1
    else:
        return 0 

#la salida es verdadera si las entradas no son iguales
def _xor(x,y):
    if x == y:
        return 0
    else:
        return 1
    
#Es la inversa de OR
def _xnor(x,y):
    if x == y:
        return 0
    else:
        return 1

def valores():
    #en esta función asignamos los valores de entrada a los circuitos manualmente
    global entrada
    entrada=[]
    puerta=""
    puerta1=False
    puerta2=False
    puerta3=False
    puerta4=False

    #creamos un while para comprobar que los datos introducidos son correctos
    while(puerta1!=True):
        print("Por favor, introduzca el valor de la primera puerta")
        puerta=int(input("Puerta 1: "))
        #comprobamos que el valor introducido es correcto
        if(puerta>1):
            print("Por favor, introduzca un valor binario (1 o 0)")
        else:
            entrada.append(puerta)
            puerta1=True

    #creamos un while para comprobar que los datos introducidos son correctos
    while(puerta2!=True):
        print("Por favor, introduzca el valor de la segunda puerta")
        puerta=int(input("Puerta 2: "))
        #comprobamos que el valor introducido es correcto
        if(puerta>1):
            print("Por favor, introduzca un valor binario (1 o 0)")
        else:
            entrada.append(puerta)
            puerta2=True

    #creamos un while para comprobar que los datos introducidos son correctos
    while(puerta3!=True):
        print("Por favor, introduzca el valor de la tercera puerta")
        puerta=int(input("Puerta 3: "))
        #comprobamos que el valor introducido es correcto
        if(puerta>1):
            print("Por favor, introduzca un valor binario (1 o 0)")
        else:
            entrada.append(puerta)
            puerta3=True

    #creamos un while para comprobar que los datos introducidos son correctos
    while(puerta4!=True):
        print("Por favor, introduzca el valor de la cuarta puerta")
        puerta=int(input("Puerta 4: "))
        #comprobamos que el valor introducido es correcto
        if(puerta>1):
            print("Por favor, introduzca un valor binario (1 o 0)")
        else:
            entrada.append(puerta)
            puerta4=True

def aleatorio():
    #en esta función asignamos los valores de entrada de los circuitos automáticamente y de manera aleatoria
    global entrada
    entrada=[]
    for i in range(4):
        aleat=random.randrange(2)
        entrada.append(aleat)

def ejercicios():
    #en esta función creamos un menú para elegir el ejercicio al que queremos acceder
    exitej=False
    while(exitej!=True):
        print("------------------------------------")
        print("------------Menú-puertas------------")
        print("------------------------------------")
        print("\n1- 2.1")
        print("2- 2.2")
        print("3- 2.3")
        print("4- 2.4")
        print("5- 2.5")
        print("6- Salir.")
        opej=int(input("Por favor, introduzca el número del ejercicio que desee ver: "))

        #Comprobamos qué opción se ha escogido
        if(opej==1):
            print("")
            ej21()
        elif(opej==2):
            print("")
            ej22()
        elif(opej==3):
            print("")
            ej23()
        elif(opej==4):
            print("")
            ej24()
        elif(opej==5):
            print("")
            ej25()
        elif(opej==6):
            print("")
            exitej=True
        else:
            print("Introduzca una opción válida!")


def ej21():
    #Realizamos el ejercicio 2.1 llamando a las funciones "and", "or" y "xnor"
    intermedio=[]
    salida=[]
    print("Bienvenidos al ejecicio 2.1: ")
    print("Puerta 1, AND: ")
    intermedio.append(_and(entrada[0], entrada[1]))
    print(intermedio[0])
    print("Puerta 2, OR: ")
    intermedio.append(_or(entrada[2], entrada[3]))
    print(intermedio[1])
    print("Puerta 3, XNOR: ")
    salida.append(_xnor(intermedio[0], intermedio[1]))
    print("Resultado: "+str(salida))

def ej22():
    #Realizamos el ejercicio 2.2 llamando a las funciones "and", "nand" y "nor"
    intermedio=[]
    salida=[]
    print("Bienvenidos al ejecicio 2.2: ")
    print("Puerta 1, AND: ")
    intermedio.append(_and(entrada[0], entrada[1]))
    print(intermedio[0])
    print("Puerta 2, NAND: ")
    intermedio.append(_nand(entrada[2], entrada[3]))
    print(intermedio[1])
    print("Puerta 3, NOR: ")
    salida.append(_nor(intermedio[0], intermedio[1]))
    print("Resultado: "+str(salida))

def ej23():
    #Realizamos el ejercicio 2.1 llamando a las funciones "xor", "and" y "or"
    intermedio=[]
    salida=[]
    print("Bienvenidos al ejecicio 2.3: ")
    print("Puerta 1, XOR: ")
    intermedio.append(_xor(entrada[0], entrada[1]))
    print(intermedio[0])
    print("Puerta 2, AND: ")
    intermedio.append(_and(entrada[2], entrada[3]))
    print(intermedio[1])
    print("Puerta 3, OR: ")
    salida.append(_or(intermedio[0], intermedio[1]))
    print("Resultado: "+str(salida))

def ej24():
    #Realizamos el ejercicio 2.1 llamando a las funciones "or", "nor" y "xnor"
    intermedio=[]
    salida=[]
    print("Bienvenidos al ejecicio 2.4: ")
    print("Puerta 1, OR: ")
    intermedio.append(_or(entrada[0], entrada[1]))
    print(intermedio[0])
    print("Puerta 2, NOR: ")
    intermedio.append(_nor(entrada[2], entrada[3]))
    print(intermedio[1])
    print("Puerta 3, XNOR: ")
    salida.append(_xnor(intermedio[0], intermedio[1]))
    print("Resultado: "+str(salida))

def ej25():
    #Realizamos el ejercicio 2.1 llamando a las funciones "nand", "or", "nor" y "not"
    intermedio=[]
    salida=[]
    print("Bienvenidos al ejecicio 2.5: ")
    print("Puerta 1, NAND: ")
    intermedio.append(_nand(entrada[0], entrada[1]))
    print(intermedio[0])
    print("Puerta 2, OR: ")
    intermedio.append(_or(entrada[2], entrada[3]))
    print(intermedio[1])
    print("Puerta 3, NOR: ")
    intermedio.append(_nor(intermedio[0], intermedio[1]))
    print(intermedio[2])
    print("Puerta 4, NOT: ")
    salida.append(_not(intermedio[2]))
    print("Resultado: "+str(salida))



exit=False
while exit!=True:
    #creamos un menú para elegir la opción queremos acceder
    print("------------------------------------")
    print("------------Menú-puertas------------")
    print("------------------------------------")
    print("\n1- Introducir valores.")
    print("2- Valores aleatorios.")
    print("3- Menú ejercicios.")
    print("4- Salir.")
    opcion=int(input("\nIntroduzca la opción deseada: "))

    #Comprobamos la opción escogida
    if(opcion==1):
        print("")
        valores()
    elif(opcion==2):
        print("")
        aleatorio()
    elif(opcion==3):
        if(len(entrada)<1):
            print("Introduzca primero valores!")
        else:
            print("")
            ejercicios()
    elif(opcion==4):
        print("")
        exit=True
    else:
        print("Introduzca una opción válida!")
