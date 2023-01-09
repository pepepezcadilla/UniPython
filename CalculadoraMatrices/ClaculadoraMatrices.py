import math


exit=False
valido=False
valido2=False
base=""
opcion=(int)
num1=0
num2=0
resultado=0
principal=0
truevalido=False
while(truevalido!=True):
    print("Desea entrar a la calculadora científica (1), a la calculadora de matrices (2) o salir (3)?")
    principal=input("1/2/3: ")
    principal=int(principal)
    if(principal==1):
        while(exit==False):
            print("Bienvenido a la Calculadora Científica Calculatrón 5000. Por favor, escoja la operación que desea realizar:")
            print("1: Suma.\n2: Resta\n3: Multiplicación\n4: División\n5: Valor absoluto\n6: Tangente\n7: Arcoseno\n8: Arcocoseno")
            print("9: Arcotangente\n10: Logaritmo en base 10\n11: Logaritmo neperiano\n12: e elevado a x\n13: Raíz cuadrada")
            print("14: Coseno Hiperbólico Inverso\n15: Número Factorial\n16: Logaritmo Gamma\n17: Máximo Común Divisor\n18: Tangente Hiperbólica\n19: Salir")
            opcion=input("Opción escogida: ")
            opcion=int(opcion)
            if(opcion==1):
                resultado=0
                print("Bienvenido a la función de suma.")
                num1=input("Introduzca el primer número: ")
                num1=int(num1)
                num2=input("Introduzca el segundo número: ")
                num2=int(num2)
                resultado= num1+num2
                print("El resultado es: "+str(resultado))
            elif(opcion==2):
                resultado=0
                print("Bienvenido a la función de resta.")
                num1=input("Introduzca el primer número: ")
                num1=int(num1)
                num2=input("Introduzca el segundo número: ")
                num2=int(num2)
                resultado= num1-num2
                print("El resultado es: "+str(resultado))
            elif(opcion==3):
                resultado=0
                print("Bienvenido a la función de multiplicación.")
                num1=input("Introduzca el primer número: ")
                num1=int(num1)
                num2=input("Introduzca el segundo número: ")
                num2=int(num2)
                resultado= num1*num2
                print("El resultado es: "+str(resultado))
            elif(opcion==4):
                resultado=0
                print("Bienvenido a la función de división.")
                num1=input("Introduzca el primer número: ")
                num1=int(num1)
                num2=input("Introduzca el segundo número: ")
                num2=int(num2)
                resultado=num1/num2
                print("El resultado es: "+str(resultado))
            elif(opcion==5):
                resultado=0
                print("Bienvenido a la función de Número absoluto.")
                num1=input("Introduzca el número que desee convertir en absoluto: ")
                num1=int(num1)
                resultado=abs(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==6):
                resultado=0
                print("Bienvenido a la función de tangente.")
                num1=input("Introduzca el número que desee conseguir la tangente: ")
                num1=float(num1)
                resultado=math.tan(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==7):
                resultado=0
                while(valido==False):
                    print("Bienvenido a la función de arcoseno.")
                    num1=input("Introduzca el número que desee conseguir el arcoseno: ")
                    num1=float(num1)
                    if(num1>(-1) and num1<1):
                        valido=True
                    else:
                        print("Por favor, introduzca un número válido (entre 1 y -1)")
                resultado=math.asin(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==8):
                resultado=0
                while(valido==False):
                    print("Bienvenido a la función de arcocoseno.")
                    num1=input("Introduzca el número que desee conseguir el arcocoseno: ")
                    num1=float(num1)
                    if(num1>(-1) and num1<1):
                        valido=True
                    else:
                        print("Por favor, introduzca un número válido (entre 1 y -1)")
                resultado=math.acos(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==9):
                resultado=0
                print("Bienvenido a la función de arcotangente.")
                num1=input("Introduzca el número que desee conseguir el arcotangente: ")
                num1=float(num1)
                resultado=math.atan(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==10):
                resultado=0
                while(valido==False):
                    print("Bienvenido a la función de logaritmo (base 10).")
                    num1=input("Introduzca el número que desee conseguir el logaritmo (base 10): ")
                    num1=float(num1)
                    if(num1<=0):
                        print("Por favor, introduzca un número válido (mayor que 0)")
                    else:
                        valido=True
                resultado=math.log10(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==11):
                valido=False
                valido2=False
                while(valido==False):
                    print("Bienvenido a la función de logaritmo.")
                    num1=input("Introduzca el número que desee conseguir el logaritmo neperiano: ")
                    num1=float(num1)
                    if(num1<=0):
                        print("Por favor, introduzca un número válido (mayor que 0)")
                    else:
                        while(valido2==False):
                            base=input("Desea cambiar la base por defecto? yes/no: ")
                            if(base=="yes"):
                                num2=input("Por favor, indique la base deseada: ")
                                num2=(float(num2))
                                if(num2<=0):
                                    print("Por favor, introduzca un número válido (mayor que 0)")
                                else:
                                    resultado=math.log(num1, num2)
                                    valido=True
                                    valido2=True
                            else:   
                                resultado=math.log(num1)
                                valido=True
                                valido2=True
                print("El resultado es: "+str(resultado))
                valido=False
                valido2=False
            elif(opcion==12):
                resultado=0
                print("Bienvenido a la función de e elevado a x.")
                num1=input("Introduzca el número: ")
                num1=int(num1)
                num2=input("Introduzca la base: ")
                num2=int(num2)
                resultado= math.pow(num1, num2)
                print("El resultado es: "+str(resultado))
            elif(opcion==13):
                resultado=0
                print("Bienvenido a la función de raíz cuadrada.")
                num1=input("Introduzca el número que desee saber la raíz cuadrada: ")
                num1=int(num1)
                resultado=math.sqrt(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==14):
                resultado=0
                valido=False
                while(valido==False):
                    print("Bienvenido a la función de Coseno Hiperbólico Inverso.")
                    num1=input("Introduzca el número que desee conseguir el coseno hiperbólico inverso: ")
                    num1=float(num1)
                    if(num1<1):
                        print("Por favor, introduzca un número válido (mayor que 1)")
                    else:
                        valido=True
                        resultado =math.acosh(num1)
                        print("El resultado es: "+str(resultado))
            elif(opcion==15):
                resultado=0
                print("Bienvenido a la función de Número factorial.")
                num1=input("Introduzca el número que desee obtener el factorial: ")
                num1=int(num1)
                resultado=math.factorial(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==16):
                resultado=0
                while(valido==False):
                    print("Bienvenido a la función de logaritmo gamma.")
                    num1=input("Introduzca el número que desee conseguir el logaritmo gamma: ")
                    num1=float(num1)
                    if(num1<=0):
                        print("Por favor, introduzca un número válido (mayor que 0)")
                    else:
                        valido=True
                resultado=math.lgamma(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==17):
                resultado=0
                print("Bienvenido a la función de máximo común divisor.")
                num1=input("Introduzca el primer número: ")
                num1=int(num1)
                num2=input("Introduzca el segundo número: ")
                num2=int(num2)
                resultado=math.gcd(num1, num2)
                print("El resultado es: "+str(resultado))
            elif(opcion==18):
                resultado=0
                print("Bienvenido a la función de tangente hiperbólica.")
                num1=input("Introduzca el número que desee conseguir la tangente hiperbólica: ")
                num1=float(num1)
                resultado=math.tanh(num1)
                print("El resultado es: "+str(resultado))
            elif(opcion==19):
                exit=True
            else:
                print("Por favor, escoja una opción.")


    elif(principal==2):
        #Menu
        exitmat=False
        while(exitmat!=True):
            print("Bienvenido a la calculadora de matrices Matricalulatrón 2000. Por favor, elija la operación que desea realizar: ")
            print("1. Suma de matrices.\n2. Reata de matrices.\n3. Multiplicación de matrices.\n4. Salir")
            menu=input("Opción escogida: ")
            menu= int(menu)
            #sucesión de if para determinar la opción
            #se pide el tamaño de la matriz
            if(menu==1 or menu==2):
                print("Por favor, introduzca el número de columnas de las matrices (mínimo 2 y máximo 5): ")
                c1=input("Número de columnas: ")
                c1=int(c1)
                print("Por favor, introduzca el número de filas de las matrices (mínimo 2 y máximo 5): ")
                f1=input("Número de filas: ")
                f1=int(f1)
                #Matriz "A"
                print ("Ingrese la Matriz A")
                af1c1=int(input("Ingrese el valor de F1C1: "))
                af1c2=int(input("Ingrese el valor de F1C2: "))
                if(c1>2):
                    af1c3=int(input("Ingrese el valor de F1C3: "))
                    if(c1>3):
                        af1c4=int(input("Ingrese el valor de F1C4: "))
                        if(c1==5):
                            af1c5=int(input("Ingrese el valor de F1C5: "))
                af2c1=int(input("Ingrese el valor de F2C1: "))
                af2c2=int(input("Ingrese el valor de F2C2: "))
                if(c1>2):
                    af2c3=int(input("Ingrese el valor de F2C3: "))
                    if(c1>3):
                        af2c4=int(input("Ingrese el valor de F2C4: "))
                        if(c1==5):
                            af2c5=int(input("Ingrese el valor de F2C5: "))
                if(f1>2):
                    af3c1=int(input("Ingrese el valor de F3C1: "))
                    af3c2=int(input("Ingrese el valor de F3C2: "))
                    if(c1>2):
                        af3c3=int(input("Ingrese el valor de F3C3: "))
                        if(c1>3):
                            af3c4=int(input("Ingrese el valor de F3C4: "))
                            if(c1==5):
                                af3c5=int(input("Ingrese el valor de F3C5: "))
                    if(f1>3):
                        af4c1=int(input("Ingrese el valor de F4C1: "))
                        af4c2=int(input("Ingrese el valor de F4C2: "))
                        if(c1>2):
                            af4c3=int(input("Ingrese el valor de F4C3: "))
                            if(c1>3):
                                af4c4=int(input("Ingrese el valor de F4C4: "))
                                if(c1==5):
                                    af4c5=int(input("Ingrese el valor de F4C5: "))
                        if(f1==5):
                            af5c1=int(input("Ingrese el valor de F5C1: "))
                            af5c2=int(input("Ingrese el valor de F5C2: "))
                            if(c1>2):
                                af5c3=int(input("Ingrese el valor de F5C3: "))
                                if(c1>3):
                                    af5c4=int(input("Ingrese el valor de F5C4: "))
                                    if(c1==5):
                                        af5c5=int(input("Ingrese el valor de F5C5: "))
                #Matriz "B"
                print ("Ingrese la Matriz B")
                bf1c1=int(input("Ingrese el valor de F1C1: "))
                bf1c2=int(input("Ingrese el valor de F1C2: "))
                if(c1>2):
                    bf1c3=int(input("Ingrese el valor de F1C3: "))
                    if(c1>3):
                        bf1c4=int(input("Ingrese el valor de F1C4: "))
                        if(c1==5):
                            bf1c5=int(input("Ingrese el valor de F1C5: "))
                bf2c1=int(input("Ingrese el valor de F2C1: "))
                bf2c2=int(input("Ingrese el valor de F2C2: "))
                if(c1>2):
                    bf2c3=int(input("Ingrese el valor de F2C3: "))
                    if(c1>3):
                        bf2c4=int(input("Ingrese el valor de F2C4: "))
                        if(c1==5):
                            bf2c5=int(input("Ingrese el valor de F2C5: "))
                if(f1>2):
                    bf3c1=int(input("Ingrese el valor de F3C1: "))
                    bf3c2=int(input("Ingrese el valor de F3C2: "))
                    if(c1>2):
                        bf3c3=int(input("Ingrese el valor de F3C3: "))
                        if(c1>3):
                            bf3c4=int(input("Ingrese el valor de F3C4: "))
                            if(c1==5):
                                bf3c5=int(input("Ingrese el valor de F3C5: "))
                    if(f1>3):
                        bf4c1=int(input("Ingrese el valor de F4C1: "))
                        bf4c2=int(input("Ingrese el valor de F4C2: "))
                        if(c1>2):
                            bf4c3=int(input("Ingrese el valor de F4C3: "))
                            if(c1>3):
                                bf4c4=int(input("Ingrese el valor de F4C4: "))
                                if(c1==5):
                                    bf4c5=int(input("Ingrese el valor de F4C5: "))
                        if(f1==5):
                            bf5c1=int(input("Ingrese el valor de F5C1: "))
                            bf5c2=int(input("Ingrese el valor de F5C2: "))
                            if(c1>2):
                                bf5c3=int(input("Ingrese el valor de F5C3: "))
                                if(c1>3):
                                    bf5c4=int(input("Ingrese el valor de F5C4: "))
                                    if(c1==5):
                                        bf5c5=int(input("Ingrese el valor de F5C5: ")) 
            if(menu==1):
                #Opcion "1" SUMA
                resultado=""
                rf1c1=af1c1 + bf1c1
                rf1c1=str(rf1c1)
                resultado="[ "+rf1c1
                rf1c2=af1c2 + bf1c2
                rf1c2=str(rf1c2)
                resultado=resultado+" "+rf1c2
                if(c1>2):
                    rf1c3=af1c3 + bf1c3
                    rf1c3=str(rf1c3)
                    resultado=resultado+" "+rf1c3
                    if(c1>3):
                        rf1c4=af1c4 + bf1c4
                        rf1c4=str(rf1c4)
                        resultado=resultado+" "+rf1c4
                        if(c1==5):
                            rf1c5=af1c5 + bf1c5
                            rf1c5=str(rf1c5)
                            resultado=resultado+" "+rf1c5
                rf2c1=af2c1 + bf2c1
                rf2c1=str(rf2c1)
                resultado=resultado+" ]\n[ "+rf2c1
                rf2c2=af2c2 + bf2c2
                rf2c2=str(rf2c2)
                resultado=resultado+" "+rf2c2
                if(c1>2):
                    rf2c3=af2c3 + bf2c3
                    rf2c3=str(rf2c3)
                    resultado=resultado+" "+rf2c3
                    if(c1>3):
                        rf2c4=af2c4 + bf2c4
                        rf2c4=str(rf2c4)
                        resultado=resultado+" "+rf2c4
                        if(c1==5):
                            rf2c5=af2c5 + bf2c5
                            rf2c5=str(rf2c5)
                            resultado=resultado+" "+rf2c5
                if(f1>2):
                    rf3c1=af3c1 + bf3c1
                    rf3c1=str(rf3c1)
                    resultado=resultado+" ]\n[ "+rf3c1
                    rf3c2=af3c2 + bf3c2
                    rf3c2=str(rf3c2)
                    resultado=resultado+" "+rf3c2
                    if(c1>2):
                        rf3c3=af3c3 + bf3c3
                        rf3c3=str(rf3c3)
                        resultado=resultado+" "+rf3c3
                        if(c1>3):
                            rf3c4=af3c4 + bf3c4
                            rf3c4=str(rf3c4)
                            resultado=resultado+" "+rf3c4
                            if(c1==5):
                                rf3c5=af3c5 + bf3c5
                                rf3c5=str(rf3c5)
                                resultado=resultado+" "+rf3c5
                    if(f1>3):
                        rf4c1=af4c1 + bf4c1
                        rf4c1=str(rf4c1)
                        resultado=resultado+" ]\n[ "+rf4c1
                        rf4c2=af4c2 + bf4c2
                        rf4c2=str(rf4c2)
                        resultado=resultado+" "+rf4c2
                        if(c1>2):
                            rf4c3=af4c3 + bf4c3
                            rf4c3=str(rf4c3)
                            resultado=resultado+" "+rf4c3
                            if(c1>3):
                                rf4c4=af4c4 + bf4c4
                                rf4c4=str(rf4c4)
                                resultado=resultado+" "+rf4c4
                                if(c1==5):
                                    rf4c5=af4c5 + bf4c5
                                    rf4c5=str(rf4c5)
                                    resultado=resultado+" "+rf4c5
                        if(f1==5):
                            rf5c1=af5c1 + bf5c1
                            rf5c1=str(rf5c1)
                            resultado=resultado+" ]\n[ "+rf5c1
                            rf5c2=af5c2 + bf5c2
                            rf5c2=str(rf5c2)
                            resultado=resultado+" "+rf5c2
                            if(c1>2):
                                rf5c3=af5c3 + bf5c3
                                rf5c3=str(rf5c3)
                                resultado=resultado+" "+rf5c3
                                if(c1>3):
                                    rf5c4=af5c4 + bf5c4
                                    rf5c4=str(rf5c4)
                                    resultado=resultado+" "+rf5c4
                                    if(c1==5):
                                        rf5c5=af5c5 + bf5c5
                                        rf5c5=str(rf5c5)
                                        resultado=resultado+" "+rf5c5
                #Visualizacion Matriz "Resultado"  
                print ("")
                print ("Matriz resultante:")
                print ("")
                print (resultado,"]")
                print ("")
            #Opcion "2" RESTA  
            if(menu==2):
                #Operacion Resta  
                resultado=""
                rf1c1=af1c1 - bf1c1
                rf1c1=str(rf1c1)
                resultado="[ "+rf1c1
                rf1c2=af1c2 - bf1c2
                rf1c2=str(rf1c2)
                resultado=resultado+" "+rf1c2
                if(c1>2):
                    rf1c3=af1c3 - bf1c3
                    rf1c3=str(rf1c3)
                    resultado=resultado+" "+rf1c3
                    if(c1>3):
                        rf1c4=af1c4 - bf1c4
                        rf1c4=str(rf1c4)
                        resultado=resultado+" "+rf1c4
                        if(c1==5):
                            rf1c5=af1c5 - bf1c5
                            rf1c5=str(rf1c5)
                            resultado=resultado+" "+rf1c5
                rf2c1=af2c1 - bf2c1
                rf2c1=str(rf2c1)
                resultado=resultado+" ]\n[ "+rf2c1
                rf2c2=af2c2 - bf2c2
                rf2c2=str(rf2c2)
                resultado=resultado+" "+rf2c2
                if(c1>2):
                    rf2c3=af2c3 - bf2c3
                    rf2c3=str(rf2c3)
                    resultado=resultado+" "+rf2c3
                    if(c1>3):
                        rf2c4=af2c4 - bf2c4
                        rf2c4=str(rf2c4)
                        resultado=resultado+" "+rf2c4
                        if(c1==5):
                            rf2c5=af2c5 - bf2c5
                            rf2c5=str(rf2c5)
                            resultado=resultado+" "+rf2c5
                            print(resultado)
                if(f1>2):
                    rf3c1=af3c1 - bf3c1
                    rf3c1=str(rf3c1)
                    resultado=resultado+" ]\n[ "+rf3c1
                    rf3c2=af3c2 - bf3c2
                    rf3c2=str(rf3c2)
                    resultado=resultado+" "+rf3c2
                    if(c1>2):
                        rf3c3=af3c3 - bf3c3
                        rf3c3=str(rf3c3)
                        resultado=resultado+" "+rf3c3
                        if(c1>3):
                            rf3c4=af3c4 - bf3c4
                            rf3c4=str(rf3c4)
                            resultado=resultado+" "+rf3c4
                            if(c1==5):
                                rf3c5=af3c5 - bf3c5
                                rf3c5=str(rf3c5)
                                resultado=resultado+" "+rf3c5
                    if(f1>3):
                        rf4c1=af4c1 - bf4c1
                        rf4c1=str(rf4c1)
                        resultado=resultado+" ]\n[ "+rf4c1
                        rf4c2=af4c2 - bf4c2
                        rf4c2=str(rf4c2)
                        resultado=resultado+" "+rf4c2
                        if(c1>2):
                            rf4c3=af4c3 - bf4c3
                            rf4c3=str(rf4c3)
                            resultado=resultado+" "+rf4c3
                            if(c1>3):
                                rf4c4=af4c4 - bf4c4
                                rf4c4=str(rf4c4)
                                resultado=resultado+" "+rf4c4
                                if(c1==5):
                                    rf4c5=af4c5 - bf4c5
                                    rf4c5=str(rf4c5)
                                    resultado=resultado+" "+rf4c5
                        if(f1==5):
                            rf5c1=af5c1 - bf5c1
                            rf5c1=str(rf5c1)
                            resultado=resultado+" ]\n[ "+rf5c1
                            rf5c2=af5c2 - bf5c2
                            rf5c2=str(rf5c2)
                            resultado=resultado+" "+rf5c2
                            if(c1>2):
                                rf5c3=af5c3 - bf5c3
                                rf5c3=str(rf5c3)
                                resultado=resultado+" "+rf5c3
                                if(c1>3):
                                    rf5c4=af5c4 - bf5c4
                                    rf5c4=str(rf5c4)
                                    resultado=resultado+" "+rf5c4
                                    if(c1==5):
                                        rf5c5=af5c5 - bf5c5
                                        rf5c5=str(rf5c5)
                                        resultado=resultado+" "+rf5c5
                #Visualizacion Matriz "Resultado"
                print ("")
                print ("Matriz resultante:")
                print ("")
                print (resultado,"]")
                print ("")
            #Opcion "3" MULTIPLICACION
            if(menu==3):
                #Operacion Multiplicacion
                resultado=""
                valido=False
                while(valido!=True):
                    print("Por favor, introduzca el número de columnas de la primera matriz (mínimo 2 y máximo 5): ")
                    c1=input("Número de columnas: ")
                    c1=int(c1)
                    print("Por favor, introduzca el número de filas de la primera matriz (mínimo 2 y máximo 5): ")
                    f1=input("Número de filas: ")
                    f1=int(f1)
                    print("Por favor, introduzca el número de columnas de la segunda matriz (mínimo 2 y máximo 5): ")
                    c2=input("Número de columnas: ")
                    c2=int(c2)
                    print("Por favor, introduzca el número de filas de la segunda matriz (mínimo 2 y máximo 5): ")
                    f2=input("Número de filas: ")
                    f2=int(f2)
                    if(c1==f2):
                        valido=True
                        #Matriz "A"
                        print ("Ingrese la Matriz A")
                        af1c1=int(input("Ingrese el valor de F1C1: "))
                        af1c2=int(input("Ingrese el valor de F1C2: "))
                        if(c1>2):
                            af1c3=int(input("Ingrese el valor de F1C3: "))
                            if(c1>3):
                                af1c4=int(input("Ingrese el valor de F1C4: "))
                                if(c1==5):
                                    af1c5=int(input("Ingrese el valor de F1C5: "))
                        af2c1=int(input("Ingrese el valor de F2C1: "))
                        af2c2=int(input("Ingrese el valor de F2C2: "))
                        if(c1>2):
                            af2c3=int(input("Ingrese el valor de F2C3: "))
                            if(c1>3):
                                af2c4=int(input("Ingrese el valor de F2C4: "))
                                if(c1==5):
                                    af2c5=int(input("Ingrese el valor de F2C5: "))
                        if(f1>2):
                            af3c1=int(input("Ingrese el valor de F3C1: "))
                            af3c2=int(input("Ingrese el valor de F3C2: "))
                            if(c1>2):
                                af3c3=int(input("Ingrese el valor de F3C3: "))
                                if(c1>3):
                                    af3c4=int(input("Ingrese el valor de F3C4: "))
                                    if(c1==5):
                                        af3c5=int(input("Ingrese el valor de F3C5: "))
                            if(f1>3):
                                af4c1=int(input("Ingrese el valor de F4C1: "))
                                af4c2=int(input("Ingrese el valor de F4C2: "))
                                if(c1>2):
                                    af4c3=int(input("Ingrese el valor de F4C3: "))
                                    if(c1>3):
                                        af4c4=int(input("Ingrese el valor de F4C4: "))
                                        if(c1==5):
                                            af4c5=int(input("Ingrese el valor de F4C5: "))
                                if(f1==5):
                                    af5c1=int(input("Ingrese el valor de F5C1: "))
                                    af5c2=int(input("Ingrese el valor de F5C2: "))
                                    if(c1>2):
                                        af5c3=int(input("Ingrese el valor de F5C3: "))
                                        if(c1>3):
                                            af5c4=int(input("Ingrese el valor de F5C4: "))
                                            if(c1==5):
                                                af5c5=int(input("Ingrese el valor de F5C5: "))
                        #Matriz "B"
                        print ("Ingrese la Matriz B")
                        bf1c1=int(input("Ingrese el valor de F1C1: "))
                        bf1c2=int(input("Ingrese el valor de F1C2: "))
                        if(c2>2):
                            bf1c3=int(input("Ingrese el valor de F1C3: "))
                            if(c2>3):
                                bf1c4=int(input("Ingrese el valor de F1C4: "))
                                if(c2==5):
                                    bf1c5=int(input("Ingrese el valor de F1C5: "))
                        bf2c1=int(input("Ingrese el valor de F2C1: "))
                        bf2c2=int(input("Ingrese el valor de F2C2: "))
                        if(c2>2):
                            bf2c3=int(input("Ingrese el valor de F2C3: "))
                            if(c2>3):
                                bf2c4=int(input("Ingrese el valor de F2C4: "))
                                if(c2==5):
                                    bf2c5=int(input("Ingrese el valor de F2C5: "))
                        if(f2>2):
                            bf3c1=int(input("Ingrese el valor de F3C1: "))
                            bf3c2=int(input("Ingrese el valor de F3C2: "))
                            if(c2>2):
                                bf3c3=int(input("Ingrese el valor de F3C3: "))
                                if(c2>3):
                                    bf3c4=int(input("Ingrese el valor de F3C4: "))
                                    if(c2==5):
                                        bf3c5=int(input("Ingrese el valor de F3C5: "))
                            if(f2>3):
                                bf4c1=int(input("Ingrese el valor de F4C1: "))
                                bf4c2=int(input("Ingrese el valor de F4C2: "))
                                if(c2>2):
                                    bf4c3=int(input("Ingrese el valor de F4C3: "))
                                    if(c2>3):
                                        bf4c4=int(input("Ingrese el valor de F4C4: "))
                                        if(c2==5):
                                            bf4c5=int(input("Ingrese el valor de F4C5: "))
                                if(f2==5):
                                    bf5c1=int(input("Ingrese el valor de F5C1: "))
                                    bf5c2=int(input("Ingrese el valor de F5C2: "))
                                    if(c2>3):
                                        bf5c3=int(input("Ingrese el valor de F5C3: "))
                                        if(c2>3):
                                            bf5c4=int(input("Ingrese el valor de F5C4: "))
                                            if(c2==5):
                                                bf5c5=int(input("Ingrese el valor de F5C5: ")) 
                        resultado="["
                        if(f1==2):
                            if(c2==2):#dos columnas por dos filas
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2

                            elif(c2==3):#tres columnas por dos filas
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                            
                            elif(c2==4):
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3
                                rf1c4=(af1c1*bf1c4)+(af1c2*bf2c4)
                                rf1c4=str(rf1c4)
                                resultado=resultado+" "+rf1c4

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                                rf2c4=(af2c1*bf1c4)+(af2c2*bf2c4)
                                rf2c4=str(rf2c4)
                                resultado=resultado+" "+rf2c4
                            
                            elif(c2==5):
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3
                                rf1c4=(af1c1*bf1c4)+(af1c2*bf2c4)
                                rf1c4=str(rf1c4)
                                resultado=resultado+" "+rf1c4
                                rf1c5=(af1c1*bf1c5)+(af1c2*bf2c5)
                                rf1c5=str(rf1c5)
                                resultado=resultado+" "+rf1c5

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                                rf2c4=(af2c1*bf1c4)+(af2c2*bf2c4)
                                rf2c4=str(rf2c4)
                                resultado=resultado+" "+rf2c4
                                rf2c5=(af2c1*bf1c5)+(af2c2*bf2c5)
                                rf2c5=str(rf2c5)
                                resultado=resultado+" "+rf2c5

                        elif(f1==3):
                            if(c2==2):#dos columnas por tres filas
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2

                            elif(c2==3):#tres columnas por dos filas

                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af2c3*bf3c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3

                            elif(c2==4):
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af1c3*bf3c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3
                                rf1c4=(af1c1*bf1c4)+(af1c2*bf2c4)+(af1c3+bf3c4)
                                rf1c4=str(rf1c4)
                                resultado=resultado+" "+rf1c4

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                                rf2c4=(af2c1*bf1c4)+(af1c2*bf2c4)+(af2c3*bf3c4)
                                rf2c4=str(rf2c4)
                                resultado=resultado+" "+rf2c4

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3
                                rf3c4=(af3c1*bf1c4)+(af1c2*bf2c4)+(af3c3*bf3c4)
                                rf3c4=str(rf3c4)
                                resultado=resultado+" "+rf3c4
                            
                            elif(c2==5):
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af1c3*bf3c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3
                                rf1c4=(af1c1*bf1c4)+(af1c2*bf2c4)+(af1c3*bf3c4)
                                rf1c4=str(rf1c4)
                                resultado=resultado+" "+rf1c4
                                rf1c5=(af1c1*bf1c5)+(af1c2*bf2c5)+(af1c3*bf3c5)
                                rf1c5=str(rf1c5)
                                resultado=resultado+" "+rf1c5

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                                rf2c4=(af2c1*bf1c4)+(af2c2*bf2c4)+(af2c3*bf3c4)
                                rf2c4=str(rf2c4)
                                resultado=resultado+" "+rf2c4
                                rf2c5=(af2c1*bf1c5)+(af2c2*bf2c5)+(af2c3*bf3c5)
                                rf2c5=str(rf2c5)
                                resultado=resultado+" "+rf2c5


                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3
                                rf3c4=(af3c1*bf1c4)+(af3c2*bf2c4)+(af3c3*bf3c4)
                                rf3c4=str(rf3c4)
                                resultado=resultado+" "+rf3c4
                                rf3c5=(af3c1*bf1c5)+(af3c2*bf2c5)+(af3c3*bf3c5)
                                rf3c5=str(rf3c5)
                                resultado=resultado+" "+rf3c5
                        elif(f1==4):
                            if(c2==2):#dos columnas por tres filas
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)+(af1c4*bf4c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)+(af1c4*bf4c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)+(af2c4*bf4c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)+(af2c4*bf4c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)+(af3c4*bf4c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)+(af3c4*bf4c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2

                                resultado=resultado+" ]\n["

                                rf4c1=(af4c1*bf1c1)+(af4c2*bf2c1)+(af4c3*bf3c1)+(af4c4*bf4c1)
                                rf4c1=str(rf4c1)
                                resultado=resultado+" "+rf4c1
                                rf4c2=(af4c1*bf1c2)+(af4c2*bf2c2)+(af4c3*bf3c2)+(af4c4*bf4c2)
                                rf4c2=str(rf4c2)
                                resultado=resultado+" "+rf4c2
                                

                            elif(c2==3):#tres columnas por dos filas

                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)+(af1c4*bf4c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)+(af1c4*bf4c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af1c3*bf3c3)+(af1c4*bf4c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)+(af2c4*bf4c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)+(af2c4*bf4c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)+(af2c4*bf4c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)+(af3c4*bf4c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)+(af3c4*bf4c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)+(af3c4*bf4c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3

                                resultado=resultado+" ]\n["

                                rf4c1=(af4c1*bf1c1)+(af4c2*bf2c1)+(af4c3*bf3c1)+(af4c4*bf4c1)
                                rf4c1=str(rf4c1)
                                resultado=resultado+" "+rf4c1
                                rf4c2=(af4c1*bf1c2)+(af4c2*bf2c2)+(af4c3*bf3c2)+(af4c4*bf4c2)
                                rf4c2=str(rf4c2)
                                resultado=resultado+" "+rf4c2                        
                                rf4c3=(af4c1*bf1c3)+(af4c2*bf2c3)+(af4c3*bf3c3)+(af4c4*bf4c3)
                                rf4c3=str(rf4c3)
                                resultado=resultado+" "+rf4c3

                            elif(c2==4):
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)+(af1c4*bf4c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)+(af1c4*bf4c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af1c3*bf3c3)+(af1c4*bf4c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3
                                rf1c4=(af1c1*bf1c4)+(af1c2*bf2c4)+(af1c3+bf3c4)+(af1c4*bf4c4)
                                rf1c4=str(rf1c4)
                                resultado=resultado+" "+rf1c4

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)+(af2c4*bf4c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)+(af2c4*bf4c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)+(af2c4*bf4c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                                rf2c4=(af2c1*bf1c4)+(af1c2*bf2c4)+(af2c3*bf3c4)+(af2c4*bf4c4)
                                rf2c4=str(rf2c4)
                                resultado=resultado+" "+rf2c4

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)+(af3c4*bf4c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)+(af3c4*bf4c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)+(af3c4*bf4c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3
                                rf3c4=(af3c1*bf1c4)+(af3c2*bf2c4)+(af3c3*bf3c4)+(af3c4*bf4c4)
                                rf3c4=str(rf3c4)
                                resultado=resultado+" "+rf3c4

                                resultado=resultado+" ]\n["

                                rf4c1=(af4c1*bf1c1)+(af4c2*bf2c1)+(af4c3*bf3c1)+(af4c4*bf4c1)
                                rf4c1=str(rf4c1)
                                resultado=resultado+" "+rf4c1
                                rf4c2=(af4c1*bf1c2)+(af4c2*bf2c2)+(af4c3*bf3c2)+(af4c4*bf4c2)
                                rf4c2=str(rf4c2)
                                resultado=resultado+" "+rf4c2                        
                                rf4c3=(af4c1*bf1c3)+(af4c2*bf2c3)+(af4c3*bf3c3)+(af4c4*bf4c3)
                                rf4c3=str(rf4c3)
                                resultado=resultado+" "+rf4c3
                                rf4c4=(af4c1*bf1c4)+(af4c2*bf2c4)+(af4c3*bf3c4)+(af4c4*bf4c4)
                                rf4c4=str(rf4c4)
                                resultado=resultado+" "+rf4c4
                            
                            elif(c2==5):
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)+(af1c4*bf4c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)+(af1c4*bf4c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af1c3*bf3c3)+(af1c4*bf4c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3
                                rf1c4=(af1c1*bf1c4)+(af1c2*bf2c4)+(af1c3*bf3c4)+(af1c4*bf4c4)
                                rf1c4=str(rf1c4)
                                resultado=resultado+" "+rf1c4
                                rf1c5=(af1c1*bf1c5)+(af1c2*bf2c5)+(af1c3*bf3c5)+(af1c4*bf4c5)
                                rf1c5=str(rf1c5)
                                resultado=resultado+" "+rf1c5

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)+(af2c4*bf4c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)+(af2c4*bf4c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)+(af2c4*bf4c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                                rf2c4=(af2c1*bf1c4)+(af2c2*bf2c4)+(af2c3*bf3c4)+(af2c4*bf4c4)
                                rf2c4=str(rf2c4)
                                resultado=resultado+" "+rf2c4
                                rf2c5=(af2c1*bf1c5)+(af2c2*bf2c5)+(af2c3*bf3c5)+(af2c4*bf4c5)
                                rf2c5=str(rf2c5)
                                resultado=resultado+" "+rf2c5


                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)+(af3c4*bf4c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)+(af3c4*bf4c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)+(af3c4*bf4c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3
                                rf3c4=(af3c1*bf1c4)+(af3c2*bf2c4)+(af3c3*bf3c4)+(af3c4*bf4c4)
                                rf3c4=str(rf3c4)
                                resultado=resultado+" "+rf3c4
                                rf3c5=(af3c1*bf1c5)+(af3c2*bf2c5)+(af3c3*bf3c5)+(af3c4*bf4c5)
                                rf3c5=str(rf3c5)
                                resultado=resultado+" "+rf3c5

                                resultado=resultado+" ]\n["

                                rf4c1=(af4c1*bf1c1)+(af4c2*bf2c1)+(af4c3*bf3c1)+(af4c4*bf4c1)
                                rf4c1=str(rf4c1)
                                resultado=resultado+" "+rf4c1
                                rf4c2=(af4c1*bf1c2)+(af4c2*bf2c2)+(af4c3*bf3c2)+(af4c4*bf4c2)
                                rf4c2=str(rf4c2)
                                resultado=resultado+" "+rf4c2                        
                                rf4c3=(af4c1*bf1c3)+(af4c2*bf2c3)+(af4c3*bf3c3)+(af4c4*bf4c3)
                                rf4c3=str(rf4c3)
                                resultado=resultado+" "+rf4c3
                                rf4c4=(af4c1*bf1c4)+(af4c2*bf2c4)+(af4c3*bf3c4)+(af4c4*bf4c4)
                                rf4c4=str(rf4c4)
                                resultado=resultado+" "+rf4c4
                                rf4c5=(af4c1*bf1c5)+(af4c2*bf2c5)+(af4c3*bf3c5)+(af4c4*bf4c5)
                                rf4c5=str(rf4c5)
                                resultado=resultado+" "+rf4c5

                        elif(f1==5):
                            if(c2==2):#dos columnas por tres filas
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)+(af1c4*bf4c1)+(af1c5*bf5c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)+(af1c4*bf4c2)+(af1c5*bf5c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)+(af2c4*bf4c1)+(af2c5*bf5c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)+(af2c4*bf4c2)+(af2c5*bf5c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)+(af3c4*bf4c1)+(af3c5*bf5c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)+(af3c4*bf4c2)+(af3c5*bf5c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2

                                resultado=resultado+" ]\n["

                                rf4c1=(af4c1*bf1c1)+(af4c2*bf2c1)+(af4c3*bf3c1)+(af4c4*bf4c1)+(af4c5*bf5c1)
                                rf4c1=str(rf4c1)
                                resultado=resultado+" "+rf4c1
                                rf4c2=(af4c1*bf1c2)+(af4c2*bf2c2)+(af4c3*bf3c2)+(af4c4*bf4c2)+(af4c5*bf5c2)
                                rf4c2=str(rf4c2)
                                resultado=resultado+" "+rf4c2

                                resultado=resultado+" ]\n["

                                rf5c1=(af5c1*bf1c1)+(af5c2*bf2c1)+(af5c3*bf3c1)+(af5c4*bf4c1)+(af5c5*bf5c1)
                                rf5c1=str(rf5c1)
                                resultado=resultado+" "+rf5c1
                                rf5c2=(af5c1*bf1c2)+(af5c2*bf2c2)+(af5c3*bf3c2)+(af5c4*bf4c2)+(af5c5*bf5c2)
                                rf5c2=str(rf5c2)
                                resultado=resultado+" "+rf5c2
                                

                            elif(c2==3):#tres columnas por dos filas

                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)+(af1c4*bf4c1)+(af1c5*bf5c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)+(af1c4*bf4c2)+(af1c5*bf5c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af1c3*bf3c3)+(af1c4*bf4c3)+(af1c5*bf5c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)+(af2c4*bf4c1)+(af2c5*bf5c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)+(af2c4*bf4c2)+(af2c5*bf5c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)+(af2c4*bf4c3)+(af2c5*bf5c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)+(af3c4*bf4c1)+(af3c5*bf5c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)+(af3c4*bf4c2)+(af3c5*bf5c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)+(af3c4*bf4c3)+(af3c5*bf5c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3

                                resultado=resultado+" ]\n["

                                rf4c1=(af4c1*bf1c1)+(af4c2*bf2c1)+(af4c3*bf3c1)+(af4c4*bf4c1)+(af4c5*bf5c1)
                                rf4c1=str(rf4c1)
                                resultado=resultado+" "+rf4c1
                                rf4c2=(af4c1*bf1c2)+(af4c2*bf2c2)+(af4c3*bf3c2)+(af4c4*bf4c2)+(af4c5*bf5c2)
                                rf4c2=str(rf4c2)
                                resultado=resultado+" "+rf4c2                        
                                rf4c3=(af4c1*bf1c3)+(af4c2*bf2c3)+(af4c3*bf3c3)+(af4c4*bf4c3)+(af4c5*bf5c3)
                                rf4c3=str(rf4c3)
                                resultado=resultado+" "+rf4c3

                                resultado=resultado+" ]\n["

                                rf5c1=(af5c1*bf1c1)+(af5c2*bf2c1)+(af5c3*bf3c1)+(af5c4*bf4c1)+(af5c5*bf5c1)
                                rf5c1=str(rf5c1)
                                resultado=resultado+" "+rf5c1
                                rf5c2=(af5c1*bf1c2)+(af5c2*bf2c2)+(af5c3*bf3c2)+(af5c4*bf4c2)+(af5c5*bf5c2)
                                rf5c2=str(rf5c2)
                                resultado=resultado+" "+rf5c2                        
                                rf5c3=(af5c1*bf1c3)+(af5c2*bf2c3)+(af5c3*bf3c3)+(af5c4*bf4c3)+(af5c5*bf5c3)
                                rf5c3=str(rf5c3)
                                resultado=resultado+" "+rf5c3

                            elif(c2==4):
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)+(af1c4*bf4c1)+(af1c5*bf5c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)+(af1c4*bf4c2)+(af1c5*bf5c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af1c3*bf3c3)+(af1c4*bf4c3)+(af1c5*bf5c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3
                                rf1c4=(af1c1*bf1c4)+(af1c2*bf2c4)+(af1c3+bf3c4)+(af1c4*bf4c4)+(af1c5*bf5c4)
                                rf1c4=str(rf1c4)
                                resultado=resultado+" "+rf1c4

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)+(af2c4*bf4c1)+(af2c5*bf5c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)+(af2c4*bf4c2)+(af2c5*bf5c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)+(af2c4*bf4c3)+(af2c5*bf5c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                                rf2c4=(af2c1*bf1c4)+(af1c2*bf2c4)+(af2c3*bf3c4)+(af2c4*bf4c4)+(af2c5*bf5c4)
                                rf2c4=str(rf2c4)
                                resultado=resultado+" "+rf2c4

                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)+(af3c4*bf4c1)+(af3c5*bf5c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)+(af3c4*bf4c2)+(af3c5*bf5c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)+(af3c4*bf4c3)+(af3c5*bf5c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3
                                rf3c4=(af3c1*bf1c4)+(af3c2*bf2c4)+(af3c3*bf3c4)+(af3c4*bf4c4)+(af3c5*bf5c4)
                                rf3c4=str(rf3c4)
                                resultado=resultado+" "+rf3c4

                                resultado=resultado+" ]\n["

                                rf4c1=(af4c1*bf1c1)+(af4c2*bf2c1)+(af4c3*bf3c1)+(af4c4*bf4c1)+(af4c5*bf5c1)
                                rf4c1=str(rf4c1)
                                resultado=resultado+" "+rf4c1
                                rf4c2=(af4c1*bf1c2)+(af4c2*bf2c2)+(af4c3*bf3c2)+(af4c4*bf4c2)+(af4c5*bf5c2)
                                rf4c2=str(rf4c2)
                                resultado=resultado+" "+rf4c2                        
                                rf4c3=(af4c1*bf1c3)+(af4c2*bf2c3)+(af4c3*bf3c3)+(af4c4*bf4c3)+(af4c5*bf5c3)
                                rf4c3=str(rf4c3)
                                resultado=resultado+" "+rf4c3
                                rf4c4=(af4c1*bf1c4)+(af4c2*bf2c4)+(af4c3*bf3c4)+(af4c4*bf4c4)+(af4c5*bf5c4)
                                rf4c4=str(rf4c4)
                                resultado=resultado+" "+rf4c4

                                resultado=resultado+" ]\n["

                                rf5c1=(af5c1*bf1c1)+(af5c2*bf2c1)+(af5c3*bf3c1)+(af5c4*bf4c1)+(af5c5*bf5c1)
                                rf5c1=str(rf5c1)
                                resultado=resultado+" "+rf5c1
                                rf5c2=(af5c1*bf1c2)+(af5c2*bf2c2)+(af5c3*bf3c2)+(af5c4*bf4c2)+(af5c5*bf5c2)
                                rf5c2=str(rf5c2)
                                resultado=resultado+" "+rf5c2                        
                                rf5c3=(af5c1*bf1c3)+(af5c2*bf2c3)+(af5c3*bf3c3)+(af5c4*bf4c3)+(af5c5*bf5c3)
                                rf5c3=str(rf5c3)
                                resultado=resultado+" "+rf5c3
                                rf5c4=(af5c1*bf1c4)+(af5c2*bf2c4)+(af5c3*bf3c4)+(af5c4*bf4c4)+(af5c5*bf5c4)
                                rf5c4=str(rf5c4)
                                resultado=resultado+" "+rf5c4
                            
                            elif(c2==5):
                                rf1c1=(af1c1*bf1c1)+(af1c2*bf2c1)+(af1c3*bf3c1)+(af1c4*bf4c1)+(af1c5*bf5c1)
                                rf1c1=str(rf1c1)
                                resultado=resultado+" "+rf1c1
                                rf1c2=(af1c1*bf1c2)+(af1c2*bf2c2)+(af1c3*bf3c2)+(af1c4*bf4c2)+(af1c5*bf5c2)
                                rf1c2=str(rf1c2)
                                resultado=resultado+" "+rf1c2
                                rf1c3=(af1c1*bf1c3)+(af1c2*bf2c3)+(af1c3*bf3c3)+(af1c4*bf4c3)+(af1c5*bf5c3)
                                rf1c3=str(rf1c3)
                                resultado=resultado+" "+rf1c3
                                rf1c4=(af1c1*bf1c4)+(af1c2*bf2c4)+(af1c3*bf3c4)+(af1c4*bf4c4)+(af1c5*bf5c4)
                                rf1c4=str(rf1c4)
                                resultado=resultado+" "+rf1c4
                                rf1c5=(af1c1*bf1c5)+(af1c2*bf2c5)+(af1c3*bf3c5)+(af1c4*bf4c5)+(af1c5*bf5c5)
                                rf1c5=str(rf1c5)
                                resultado=resultado+" "+rf1c5

                                resultado=resultado+" ]\n["

                                rf2c1=(af2c1*bf1c1)+(af2c2*bf2c1)+(af2c3*bf3c1)+(af2c4*bf4c1)+(af2c5*bf5c1)
                                rf2c1=str(rf2c1)
                                resultado=resultado+" "+rf2c1
                                rf2c2=(af2c1*bf1c2)+(af2c2*bf2c2)+(af2c3*bf3c2)+(af2c4*bf4c2)+(af2c5*bf5c2)
                                rf2c2=str(rf2c2)
                                resultado=resultado+" "+rf2c2
                                rf2c3=(af2c1*bf1c3)+(af2c2*bf2c3)+(af2c3*bf3c3)+(af2c4*bf4c3)+(af2c5*bf5c3)
                                rf2c3=str(rf2c3)
                                resultado=resultado+" "+rf2c3
                                rf2c4=(af2c1*bf1c4)+(af2c2*bf2c4)+(af2c3*bf3c4)+(af2c4*bf4c4)+(af2c5*bf5c4)
                                rf2c4=str(rf2c4)
                                resultado=resultado+" "+rf2c4
                                rf2c5=(af2c1*bf1c5)+(af2c2*bf2c5)+(af2c3*bf3c5)+(af2c4*bf4c5)+(af2c5*bf5c5)
                                rf2c5=str(rf2c5)
                                resultado=resultado+" "+rf2c5


                                resultado=resultado+" ]\n["

                                rf3c1=(af3c1*bf1c1)+(af3c2*bf2c1)+(af3c3*bf3c1)+(af3c4*bf4c1)+(af3c5*bf5c1)
                                rf3c1=str(rf3c1)
                                resultado=resultado+" "+rf3c1
                                rf3c2=(af3c1*bf1c2)+(af3c2*bf2c2)+(af3c3*bf3c2)+(af3c4*bf4c2)+(af3c5*bf5c2)
                                rf3c2=str(rf3c2)
                                resultado=resultado+" "+rf3c2                        
                                rf3c3=(af3c1*bf1c3)+(af3c2*bf2c3)+(af3c3*bf3c3)+(af3c4*bf4c3)+(af3c5*bf5c3)
                                rf3c3=str(rf3c3)
                                resultado=resultado+" "+rf3c3
                                rf3c4=(af3c1*bf1c4)+(af3c2*bf2c4)+(af3c3*bf3c4)+(af3c4*bf4c4)+(af3c5*bf5c4)
                                rf3c4=str(rf3c4)
                                resultado=resultado+" "+rf3c4
                                rf3c5=(af3c1*bf1c5)+(af3c2*bf2c5)+(af3c3*bf3c5)+(af3c4*bf4c5)+(af3c5*bf5c5)
                                rf3c5=str(rf3c5)
                                resultado=resultado+" "+rf3c5

                                resultado=resultado+" ]\n["

                                rf4c1=(af4c1*bf1c1)+(af4c2*bf2c1)+(af4c3*bf3c1)+(af4c4*bf4c1)+(af4c5*bf5c1)
                                rf4c1=str(rf4c1)
                                resultado=resultado+" "+rf4c1
                                rf4c2=(af4c1*bf1c2)+(af4c2*bf2c2)+(af4c3*bf3c2)+(af4c4*bf4c2)+(af4c5*bf5c2)
                                rf4c2=str(rf4c2)
                                resultado=resultado+" "+rf4c2                        
                                rf4c3=(af4c1*bf1c3)+(af4c2*bf2c3)+(af4c3*bf3c3)+(af4c4*bf4c3)+(af4c5*bf5c3)
                                rf4c3=str(rf4c3)
                                resultado=resultado+" "+rf4c3
                                rf4c4=(af4c1*bf1c4)+(af4c2*bf2c4)+(af4c3*bf3c4)+(af4c4*bf4c4)+(af4c5*bf5c4)
                                rf4c4=str(rf4c4)
                                resultado=resultado+" "+rf4c4
                                rf4c5=(af4c1*bf1c5)+(af4c2*bf2c5)+(af4c3*bf3c5)+(af4c4*bf4c5)+(af4c5*bf5c5)
                                rf4c5=str(rf4c5)
                                resultado=resultado+" "+rf4c5

                                resultado=resultado+" ]\n["

                                rf5c1=(af5c1*bf1c1)+(af5c2*bf2c1)+(af5c3*bf3c1)+(af5c4*bf4c1)+(af5c5*bf5c1)
                                rf5c1=str(rf5c1)
                                resultado=resultado+" "+rf5c1
                                rf5c2=(af5c1*bf1c2)+(af5c2*bf2c2)+(af5c3*bf3c2)+(af5c4*bf4c2)+(af5c5*bf5c2)
                                rf5c2=str(rf5c2)
                                resultado=resultado+" "+rf5c2                        
                                rf5c3=(af5c1*bf1c3)+(af5c2*bf2c3)+(af5c3*bf3c3)+(af5c4*bf4c3)+(af5c5*bf5c3)
                                rf5c3=str(rf5c3)
                                resultado=resultado+" "+rf5c3
                                rf5c4=(af5c1*bf1c4)+(af5c2*bf2c4)+(af5c3*bf3c4)+(af5c4*bf4c4)+(af5c5*bf5c4)
                                rf5c4=str(rf5c4)
                                resultado=resultado+" "+rf5c4
                                rf5c5=(af5c1*bf1c5)+(af5c2*bf2c5)+(af5c3*bf3c5)+(af5c4*bf4c5)+(af5c5*bf5c5)
                                rf5c5=str(rf5c5)
                                resultado=resultado+" "+rf5c5

                        #Visualizacion Matriz "Resultado"
                        print ("")
                        print ("Matriz resultante:")
                        print ("")
                        print (resultado,"]")
                        print ("")
                    else:
                        print("Por favor, introduzca un valor válido")
            if(menu==4):
                print("Desea salir?")
                salirmatr=input("yes/no: ")
                if(salirmatr=="yes"):
                    exitmat=True
    elif(principal==3):
        print("Desea salir?")
        truexit=input("yes/no: ")
        if(truexit=="yes"):
            truevalido=True
