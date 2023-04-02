import math


exit=False
valido=False
valido2=False
base=""
opcion=(int)
num1=0
num2=0
resultado=0
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
    elif(opcion==18):
        exit=True
    else:
        print("Por favor, escoja una opción.")