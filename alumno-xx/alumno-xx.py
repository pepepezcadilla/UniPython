import math

#Declaración de variables globales
exit=False
valido=False
valido2=False
base=""
opcion=(int)
num1=0
num2=0
resultado=0
clave="immune"
pi=int(3.141592653589793)

#Definimos la función para introducir la contraseña.
def ClaveAcceso():
    boolpass=False
    cont=0
    #Creamos un while para que no sea válida cualquier contraseña, y tener 3 intentos
    while(boolpass!=True):
        passw=input("Introduzca la contraseña por favor: ")
        if(passw==clave):
            print("Contraseña correcta!")
            menuPrincipal()
        else:
            cont=cont+1
            print("Contraseña incorrecta!")
            if(cont>=3):
                break

#Definimos la funcion del menú principal, la cual permite cambiar la clave o acceder a la calculadora
def menuPrincipal():
    boolprinc=False
    while(boolprinc!=True):
        print("**************************************************************")
        print("******************* CALCULADORA CIENTÍFICA *******************")
        print("**************************************************************")
        print("                         ACCESO USUARIO")
        print("**************************************************************")
        print("\n\n1- Modificar Clave")
        print("2- Calculadora Científica\n")
        opcionprinc=input()
        #Una secuencia de if para determinar la opción escogida
        if(opcionprinc=="1"):
            boolprinc=True
            cambiaClave()
        elif(opcionprinc=="2"):
            boolprinc=True
            menucalcs()
        else:
            print("Introduzca una opción correcta.")

#definimos la función para cambiar la clave
def cambiaClave():
    print("Cambio de Contraseña")
    newpass=input("Introduzca la nueva contraseña: ")
    clave=newpass
    menuPrincipal()

#declaración de la función que te permite ir a una calculadora o a otra
def menucalcs():
    boolcalcs=False
    while(boolcalcs!=True):
        print("**************************************************************")
        print("******************* CALCULADORA CIENTÍFICA *******************")
        print("**************************************************************")
        print("                         MENU PRINCIPAL")
        print("**************************************************************")
        print("\n\n1- Operaciones Aritméticas")
        print("2- Operaciones con matrices")
        print("3- Busqueda")
        print("4- Apagar CC\n")
        opcioncalcs=input()
        #Una secuencia de if para determinar la opción escogida
        if(opcioncalcs=="1"):
            menu()
        elif(opcioncalcs=="2"):
            menuMatriz()
        elif(opcioncalcs=="3"):
            busqueda()
        elif(opcioncalcs=="4"):
            print("APAGANDO")
            break
        else:
            print("Introduzca una opción correcta.")

#Declaración de la función menú
def menu(): 
    print("**************************************************************")
    print("******************* CALCULADORA CIENTÍFICA *******************")
    print("**************************************************************")
    print("                         MENU PRINCIPAL")
    print("**************************************************************")
    print("1: Suma.\n2: Resta\n3: Multiplicación\n4: División\n5: Valor absoluto\n6: Seno\n7: Coseno\n8: Tangente\n9: Arcoseno")
    print("10: Arcocoseno\n11: Arcotangente\n12: Logaritmo en base 10\n13: Logaritmo neperiano\n14: e elevado a x\n15: Raíz cuadrada\n16: Salir")
    opcion=int(input("Opción escogida: "))
    #Una secuencia de if para determinar la opción escogida
    if(opcion==1):
        resultado=0
        print("Bienvenido a la función de suma.")
        print("Cúantos números desea sumar?")
        cantidad=input()
        cantidad=int(cantidad)
        #creamos un array para almacenar los operadores
        numeros= []
        for x in range(cantidad):
            print("Introduzca el número " +str(x+1)+": ")
            num1=input()
            num1=int(num1)
            #recogemos los operadores y los introducimos en el array.
            numeros.append(num1)
        #Llamamos a la función suma y le pasamos el array de operadores.
        resultado=suma(numeros)
        print("El resultado es: "+str(resultado))

    elif(opcion==2):
        resultado=0
        print("Bienvenido a la función de resta.")
        print("Cúantos números desea restar?")
        cantidad=input()
        cantidad=int(cantidad)
        #creamos un array para almacenar los operadores
        numeros= []
        for x in range(cantidad):
            print("Introduzca el número " +str(x+1)+": ")
            num1=input()
            num1=int(num1)
            #recogemos los operadores y los introducimos en el array.
            numeros.append(num1)
        #Llamamos a la función resta y le pasamos el array de operadores.
        resultado=resta(numeros)
        print("El resultado es: "+str(resultado))

    elif(opcion==3):
        resultado=0
        print("Bienvenido a la función de multiplicación.")
        print("Cúantos números desea multiplicar?")
        cantidad=input()
        cantidad=int(cantidad)
        #creamos un array para almacenar los operadores
        numeros= []
        for x in range(cantidad):
            print("Introduzca el número " +str(x+1)+": ")
            num1=input()
            num1=int(num1)
            #recogemos los operadores y los introducimos en el array.
            numeros.append(num1)
        #Llamamos a la función multipl y le pasamos el array de operadores.
        resultado=multipl(numeros)
        print("El resultado es: "+str(resultado))

    elif(opcion==4):
        resultado=0
        print("Bienvenido a la función de división.")
        num1=input("Introduzca el primer número: ")
        num1=int(num1)
        num2=input("Introduzca el segundo número: ")
        num2=int(num2)
        #Llamamos a la función division y le pasamos los dos operadores.
        resultado=division(num1, num2)
        print("El resultado es: "+str(resultado))

    elif(opcion==5):
        resultado=0
        print("Bienvenido a la función de Número absoluto.")
        num1=input("Introduzca el número que desee convertir en absoluto: ")
        num1=int(num1)
        #Llamamos a la función absolute y le pasamos el operador.
        resultado=absolute(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==6):
        resultado=0
        print("Bienvenido a la función de seno.")
        num1=input("Introduzca el número que desee conseguir el seno: ")
        num1=float(num1)
        #Llamamos a la función tangente y le pasamos el operador.
        resultado=seno(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==7):
        resultado=0
        print("Bienvenido a la función de coseno.")
        num1=input("Introduzca el número que desee conseguir el coseno: ")
        num1=float(num1)
        #Llamamos a la función tangente y le pasamos el operador.
        resultado=coseno(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==8):
        resultado=0
        print("Bienvenido a la función de tangente.")
        num1=input("Introduzca el número que desee conseguir la tangente: ")
        num1=float(num1)
        #Llamamos a la función tangente y le pasamos el operador.
        resultado=tangente(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==9):
        resultado=0
        print("Bienvenido a la función de arcoseno.")
        num1=input("Introduzca el número que desee conseguir el arcoseno: ")
         #Llamamos a la función arco y le pasamos el operador.
        resultado=arco(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==10):
        resultado=0
        print("Bienvenido a la función de arcocoseno.")
        num1=input("Introduzca el número que desee conseguir el arcocoseno: ")
        #Llamamos a la función arcoco y le pasamos el operador.
        resultado=arcocos(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==11):
        resultado=0
        print("Bienvenido a la función de arcotangente.")
        num1=input("Introduzca el número que desee conseguir el arcotangente: ")
        num1=float(num1)
        #Llamamos a la función atangente y le pasamos el operador.
        resultado=atangente(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==12):
        resultado=0
        valido=False
        while(valido==False):
            #Creamos un bucle para comprobar si el número introducido es correcto
            print("Bienvenido a la función de logaritmo (base 10).")
            num1=input("Introduzca el número que desee conseguir el logaritmo (base 10): ")
            num1=float(num1)
            #Comprobamos si el número introducido es correcto
            if(num1<=0):
                print("Por favor, introduzca un número válido (mayor que 0)")
            else:
                valido=True
        #Llamamos a la función logadiez y le pasamos el operador.
        resultado=logadiez(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==13):
        valido=False
        while(valido==False):
            #Creamos un bucle para comprobar si el número introducido es correcto
            print("Bienvenido a la función de logaritmo.")
            num1=input("Introduzca el número que desee conseguir el logaritmo neperiano: ")
            num1=float(num1)
            #Comprobamos si el número introducido es correcto
            if(num1<=0):
                print("Por favor, introduzca un número válido (mayor que 0)")
            else:
                valido=True
                #Llamamos a la función loga y le pasamos el operador.
                resultado=loga(num1)
        print("El resultado es: "+str(resultado))
        valido=False

    elif(opcion==14):
        resultado=0
        print("Bienvenido a la función de e elevado a x.")
        num1=input("Introduzca el número: ")
        num1=int(num1)
        num2=input("Introduzca la base: ")
        num2=int(num2)
        #Llamamos a la función potencia y le pasamos los operadores.
        resultado= potencia(num1, num2)
        print("El resultado es: "+str(resultado))

    elif(opcion==15):
        resultado=0
        print("Bienvenido a la función de raíz cuadrada.")
        num1=input("Introduzca el número que desee saber la raíz cuadrada: ")
        num1=int(num1)
        #Llamamos a la función raiz y le pasamos el operador.
        resultado=raiz(num1)
        print("El resultado es: "+str(resultado))

    elif(opcion==16):
        print("Saliendo")
        #Salimos del bucle while.
        return True
    else:
        print("Por favor, escoja una opción.")

#Declaración de la función menú
def menuMatriz():
    print("**************************************************************")
    print("******************* CALCULADORA CIENTÍFICA *******************")
    print("**************************************************************")
    print("                         MENU MATRICES")
    print("**************************************************************")
    print("\n\n1- Suma de matrices")
    print("2- Resta de matrices")
    print("3- Multiplicación de matrices")
    menu=input("Opción escogida: ")
    menu= int(menu)
    #se crean dos array para almacenar las matrices
    matriz=[]
    matriz2=[]
    #se pide el tamaño de la matriz
    validouno=False
    while(validouno!=True):
        print("Por favor, introduzca el tamaño de las matrices(mínimo 2 y máximo 3): ")
        m1=input("Número de columnas: ")
        m1=int(m1)
        if(m1>3 or m1<1):
            print("Introduzca un valor correcto.")
            validouno=False
        else:
            validouno=True
    for i in range(m1):
        #Se crea un array para ir almacenando los valores de cada fila
        fila=[]
        for x in range(m1):
            print("Introduzca el valor "+str(x+1)+" de la fila "+str(i+1)+" de la primera matriz")
            var=input()
            var=int(var)
            #Se recoge un valor y se introduce en el array fila[]
            fila.append(var)  
        #Se introduce el array fila[] en el array matriz[] para hacerlo bidimensional
        matriz.append(fila)
    print("")

    for i in range(m1):
        #Se crea un array para ir almacenando los valores de cada fila
        filados=[]
        for x in range(m1):
            print("Introduzca el valor "+str(x+1)+" de la fila "+str(i+1)+" de la segunda matriz")
            var=input()
            var=int(var)
            #Se recoge un valor y se introduce en el array fila[]
            filados.append(var) 
        #Se introduce el array fila[] en el array matriz[] para hacerlo bidimensional 
        matriz2.append(filados)

    #Una secuencia de if para determinar la opción escogida
    if(menu==1):
        #se crea un array para almacenar la matriz resultado
        matrizresult=[]
        for i in range(m1):
            #Se crea un array para ir almacenando los valores de cada fila
            filares=[]
            for x in range(m1):
                #se suman los valores de las dos matrices y se van almacenando en el array filares[]
                res=matriz[i][x]+matriz2[i][x]
                filares.append(res)
            #Se añade el array filares[] al array matrizresult[]
            matrizresult.append(filares)
        print("Matriz resultante: ")
        for i in range(m1):
            for x in range(m1):
                print(matrizresult[i][x], end=" ")
            print("")
        print("")

    if(menu==2):
        #se crea un array para almacenar la matriz resultado
        matrizresult=[]
        for i in range(m1):
            #Se crea un array para ir almacenando los valores de cada fila
            filares=[]
            for x in range(m1):
                #se suman los valores de las dos matrices y se van almacenando en el array filares[]
                res=matriz[i][x]-matriz2[i][x]
                filares.append(res)
            #Se añade el array filares[] al array matrizresult[]
            matrizresult.append(filares)
        #Se muestra por pantalla la matriz resultante
        print("Matriz resultante: ")
        for i in range(m1):
            for x in range(m1):
                print(matrizresult[i][x], end=" ")
            print("")
        print("")

    if(menu==3):
        #se crea un array para almacenar la matriz resultado
        matrizresult=[]
        for i in range(m1):
            #Inicializamos todos los valores del array, lo hacemos de dos dimensiones y asignamos un valor vacío a cada posición
            matrizresult.append([])
            for x in range(m1):
                matrizresult[i].append("")
        for y in range(m1):
            for i in range(m1):
                for x in range(m1):
                    #Multiplicamos los valores de las dos matrices
                    res=matriz[i][x]*matriz2[x][y]
                #Vamos asignando a cada posición del array el valor de res
                matrizresult[i][y]=res
        #Se muestra por pantalla la matriz resultante
        print("Matriz resultante: ")
        for i in range(m1):
            for x in range(m1):
                print(matrizresult[i][x], end=" ")
            print("")
        print("")

#Declaración de la función busqueda
def busqueda():
    print("**************************************************************")
    print("******************* CALCULADORA CIENTÍFICA *******************")
    print("**************************************************************")
    print("                         BUSQUEDA")
    print("**************************************************************")
    print("\n\n1- Mayor")
    print("2- Menor")
    print("3- Media\n")
    opcion=int(input("Opción escogida: "))
    comprobus=False
    #Comprobamos que el valor introducido es válido
    while(comprobus!=True):
        if(opcion>3 or opcion<1):
            print("introduzca un valor válido.")
            opcion=int(input("Opción escogida: "))
        else:
            comprobus=True
    #Creamos un array y le asignamos los 10 
    busqueda=[]
    for i in range(10):
        busqueda.append(int(input("Introduzca el número "+str(i+1)+": ")))
    
    #Una secuencia de if para determinar la opción escogida (de otra manera que en los anteriores menús)
    if(opcion==1):
        #Vamos comparando todas las posiciones del array con la mayor hasta el momento
        mayor=busqueda[0]
        for i in range(10):
            if(mayor<busqueda[i]):
                mayor=busqueda[i]
        print("El mayor número es el "+str(mayor))

    if(opcion==2):
        #Vamos comparando todas las posiciones del array con la menor hasta el momento
        menor=busqueda[0]
        for i in range(10):
            if(menor>busqueda[i]):
                menor=busqueda[i]
        print("El menor número es el "+str(menor))

    if(opcion==3):
        #Sumamos todas las posiciones del array y lo dividimos entre 10
        media=0
        for i in range(10):
            media=media+busqueda[i]
        print("La media es: "+str(media/10))


#Definición de las variables operativas.

def suma(numeros):
    resultado=0
    for i in range(len(numeros)):
       resultado=resultado+numeros[i]
    return resultado

def resta(numeros):
    resultado=numeros[0]
    for i in range(len(numeros)-1):
       resultado=resultado-numeros[i+1]
    return resultado

def multipl(numeros):
    resultado=numeros[0]
    for i in range(len(numeros)-1):
       resultado=resultado*numeros[i+1]
    return resultado

def division(numero1, numero2):
    return numero1/numero2

def absolute(numero1):
    return abs(numero1)

def seno(numero1):
    return math.sin(int(numero1))

def coseno(numero1):
    return math.cos(int(numero1))

def tangente(numero1):
    sine=seno(numero1)
    cosine=coseno(numero1)
    tang=sine/cosine
    return tang

def arco(numero1):
    arcosine=1/seno(numero1)
    return arcosine

def arcocos(numero1):
    arcocosine=1/coseno(numero1)
    return grados(int(arcocosine))

def atangente(numero1):
    arcotang=1/tangente(numero1)
    return arcotang

def logadiez(numero1):
    return math.log10(numero1)

def loga(numero1):
    valido2=False
    #Creamos un bucle para comprobar si el número introducido es correcto
    while(valido2==False):
        base=input("Desea cambiar la base por defecto? yes/no: ")
        if(base=="yes"):
            numero2=input("Por favor, indique la base deseada: ")
            numero2=(float(numero2))
            #Comprobamos si el número introducido es correcto
            if(numero2<=0):
                print("Por favor, introduzca un número válido (mayor que 0)")
            else:
                valido2=True
                return math.log(numero1, numero2)
        else:   
            valido2=True
            return math.log(numero1)
                        
def potencia(numero1, numero2):
    return math.pow(numero1, numero2)

def raiz(numero1):
    return math.sqrt(numero1)

def radianes(numero):
    res=(pi*numero)/180
    return res

def grados(numero):
    res=(180*numero)/pi
    return res

#Llamamos a la función ClaveAcceso() para empezar el programa.
ClaveAcceso()