def menu():
    exit=False
    while(exit!=True):
        var=2
        print("------------------------------------")
        print("---------Menú-ejercicios------------")
        print("------------------------------------")
        print("\n1- Ejercicio 1")
        print("2- Ejercicio 2")
        print("3- Ejercicio 3")
        print("4- Ejercicio 4")
        print("5- Ejercicio 5")
        print("6- Ejercicio 6")
        print("7- Ejercicio 7")
        print("8- Ejercicio 8")
        print("9- Ejercicio 9")
        print("10- Ejercicio 10")
        print("11- Ejercicio 11")
        print("12- Salir")
        opcion=int(input("Por favor, introduzca la opcion deseada: "))

        if(opcion==1):
            ej1()
        elif(opcion==2):
            ej2()
        elif(opcion==3):
            ej3()
        elif(opcion==4):
            ej4()
        elif(opcion==5):
            ej5()
        elif(opcion==6):
            ej6()
        elif(opcion==7):
            ej7()
        elif(opcion==8):
            ej8()
        elif(opcion==9):
            ej9()
        elif(opcion==10):
            ej10()
        elif(opcion==11):
            ej11()
        elif(opcion==12):
            exit=True
        else:
            print("Introduzca un número válido!")

def ej1():
    fichero = open("ficheroE1.txt", "w")
    fichero.write("Este es mi primer programa de fichero y lo he escrito en python usando la forma clásica:")
    fichero.close
    print("Terminado!")

def ej2():
    with open("ficheroE2.txt", "w") as fichero: 
        fichero.write("Este es mi segundo programa de fichero y lo he escrito en python usando la forma recomendada:")
        fichero.close
    print("Terminado!")

def ej3():
    with open("ejercicio3-100.txt", "w") as fichero:
        valido=False
        while(valido!=True):
            numero=int(input("Introduzca un número positivo entre 1 y 100 por favor: "))
            if(numero<1 or numero>100):
                print("Introduzca un número correcto!")
                valido=False
            else:
                fichero.write(str(numero))
                valido=True
        fichero.close
    print("Terminado!")

def ej4():
    with open("ejercicio4-tabla.txt", "a") as fichero:
        valido=False
        while(valido!=True):
            numero=int(input("Introduzca el número del que quiera sacar la tabla de multiplicar: "))
            if(numero<1 or numero>10):
                print("Introduzca un número correcto!")
                valido=False
            else:
                valido=True
        for i in range(10):
            fichero.write(str(numero)+"x"+str(i+1)+"="+str(numero*(i+1))+"\n")
        fichero.close
    print("Terminado!")

def ej5():
    with open("ejercicio5-tabla.txt", "a") as fichero:
        valido=False
        while(valido!=True):
            numero=int(input("Introduzca el número del que quiera sacar la tabla de multiplicar: "))
            if(numero<1 or numero>10):
                print("Introduzca un número correcto!")
                valido=False
            else:
                valido=True
        for i in range(numero):
            fichero.write("Tabla del "+str(i+1)+"\n")
            for j in range(numero):
                fichero.write(str(i+1)+"x"+str(j+1)+"="+str((i+1)*(j+1))+"\n")
        fichero.close
    print("Terminado!")

def ej6():

    valido=False
    while(valido!=True):
        numero=int(input("Introduzca el número del que quiera sacar la tabla de multiplicar: "))
        if(numero<1 or numero>10):
            print("Introduzca un número correcto!")
            valido=False
        else:
            valido=True
    with open("ejercicio4-tabla del-"+str(numero)+".txt", "a") as fichero:
        for i in range(10):
            fichero.write(str(numero)+"x"+str(i+1)+"="+str(numero*(i+1))+"\n")
        fichero.close
    print("Terminado!")

def ej7():
    valido=False
    while(valido!=True):
        numero=int(input("Introduzca el número del que quiera sacar la tabla de multiplicar: "))
        if(numero<1 or numero>10):
            print("Introduzca un número correcto!")
            valido=False
        else:
            valido=True
    try:
        with open("fichero-tabla-del-"+str(numero)+".txt", "r") as fichero:
            leer=fichero.read()
            print(leer)
    except FileNotFoundError:
        print("Fichero no encontrado.")

def ej8():
    valido=False
    while(valido!=True):
        numero=int(input("Introduzca las líneas que desee leer: "))
        if(numero<0):
            print("Introduzca un número correcto!")
            valido=False
        else:
            valido=True
    with open("ejercicio4-tabla.txt", "r") as fichero:
        for i in range(numero):
            leer=fichero.readline()
            print(leer, end="")

def ej9():
    valido=False
    while(valido!=True):
        numero=int(input("Introduzca la línea a partir de la cual desee leer: "))
        if(numero<0):
            print("Introduzca un número correcto!")
            valido=False
        else:
            valido=True
    with open("ejercicio4-tabla.txt", "r") as fichero:
        count=len(fichero.readlines())
        fichero.seek(0)
        for i in range(count):
            leer=fichero.readline()
            if(i>=numero):
                print(leer, end="")

def ej10():
    with open("ejercicio4-tabla.txt", "r") as fichero:
        count=len(fichero.readlines())
        print("El documento tiene "+str(count)+" líneas.")

def ej11():
    matriceria("matriz1", "primera")
    matriceria("matriz2", "segunda")
    matriz1=leematriz("matriz1")
    matriz2=leematriz("matriz2")
    resultado=[]

    for i in range(3):
        fila=[]
        for x in range(3):
            fila.append((int(matriz1[i][x])+int(matriz2[i][x])))
        resultado.append(fila)
    
    print("La matriz resultante es:\n["+str(resultado[0][0])+" "+str(resultado[0][1])+" "+str(resultado[0][2]))
    print(" "+str(resultado[1][0])+" "+str(resultado[1][1])+" "+str(resultado[1][2]))
    print(" "+str(resultado[2][0])+" "+str(resultado[2][1])+" "+str(resultado[2][2])+"]")

    with open("resultado.txt", "w") as fichero:
        for i in range(3):
            for x in range(3):
                numero=resultado[i][x]
                fichero.write(str(numero)+" ")
            fichero.write("\n")
def matriceria(nombrefichero, numeromatriz):
    matriz=[]
    
    for i in range(3):
        #Se crea un array para ir almacenando los valores de cada fila
        fila=[]
        for x in range(3):
            valido=False
            while(valido!=True):
                print("Introduzca el valor "+str(x+1)+" de la fila "+str(i+1)+" de la "+numeromatriz+" matriz")
                numero=input()
                numero=int(numero)
                if(numero<(-99) or numero>99):
                    print("Introduzca un número correcto!")
                    valido=False
                else:
                    valido=True
            #Se recoge un valor y se introduce en el array fila[]
            fila.append(numero)  
        #Se introduce el array fila[] en el array matriz[] para hacerlo bidimensional
        matriz.append(fila)
    print("")
    with open(nombrefichero+".txt", "w") as fichero:
        for i in range(3):
            for x in range(3):
                numero=matriz[i][x]
                fichero.write(str(numero)+" ")
            fichero.write("\n")

def leematriz(nombrefichero):
    matriz=[]
    with open(nombrefichero+".txt", "r") as fichero:
        for i in range(3):
            fila=fichero.readline()
            fila=str(fila)
            fila=fila.split()
            matriz.append(fila)
    return matriz
menu()