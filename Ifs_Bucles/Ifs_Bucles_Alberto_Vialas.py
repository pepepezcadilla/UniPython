menu=0
truexit=False #creamos un bucle para el menú
while(truexit!=True):
    print("Introduzca el ejercicio deseado: \n1. Número ganador\n2. Menor entre dos numeros\n3. Menor o igual entre dos números\n4. Días de la semana\n5. Número absoluto\n6. Partidos políticos\n7. Vocales\n8. Palabra 10 veces.\n9. Edad\n10. Números impares\n11. Números invertidos\n12. Continuar con el programa\n13. Triángulo\n14. Tabla del 10\n15. Programa eco\n16. Contraseña\n17.Triángulo de impares\n18. Hucha\n19. Hucha con opción de sacar dinero\n20. Palabra al revés\n21. Letra dentro de una frase\n22. Exit")
    menu=input("Número: ")
    menu=int(menu)
    if(menu==1): #solicitamos al usuario un número, lo comparamos a 1000, y si es igual, mostramos "ganaste un premio" por pantalla.
        numero=input("Introduzca un número de cliente: ")
        numero=int(numero)
        if(numero==1000):
            print("Ganaste un premio")
    elif(menu==2): #solicitamos al usuario que introduzca dos números, los comparamos y decimos cual es el menor.
        numero1=input("Introduzca el primer número: ")
        numero1=int(numero1)
        numero2=input("Introduzca el segundo número: ")
        numero2=int(numero2)
        if(numero1<numero2):
            print(str(numero1)+" es el número menor.")
        else:
            print(str(numero2)+" es el número menor.")
    elif(menu==3): #solicitamos al usuario que introduzca dos números, los comparamos, y decimos cual es el menor, o si son iguales.
        numero1=input("Introduzca el primer número: ")
        numero1=int(numero1)
        numero2=input("Introduzca el segundo número: ")
        numero2=int(numero2)
        if(numero1<numero2):
            print(str(numero1)+" es el número menor.")
        elif(numero1==numero2):
            print("Ambos números son iguales")
        elif(numero1>numero2):
            print(str(numero2)+" es el número menor.")
    elif(menu==4): #solicitamos al usuario un día de la semana. Comprobamos qué día ha introducido. Si es lunes, mostramos el mensaje A. Si es viernes, el mensaje B. Si es sábado "or" domingo, el mensaje C. Si es otro día, el mensaje D.
        dia=input("Introduzca un día de la semana: ")
        if(dia=="lunes"):
            print("Hay que empezar la semana con alegría! :D")
        elif(dia=="viernes"):
            print("Ya no hay que trabajar! Ahora a disfrutar!")
        elif(dia=="sabado" or dia=="domingo"):
            print("Feliz fin de semana!!")
        else: 
            print("Ánimo, que ya queda menos!")
    elif(menu==5): #solicitamos al usuario un número, y lo convertimos a su absoluto con "abs(numero)"
        numero=input("Introduzca un número: ")
        numero=int(numero)
        resultado=abs(numero)
        print("El número absoluto de "+str(numero)+" es: "+str(resultado))
    elif(menu==6): #solicitamos al usuario una letra. Comprobamos cuál ha introducido. Si es A, mostramos el mensaje A. Si es B, mostramos el mensaje B. Si es C, mostramos el mensaje C. Si no, aparece "Opcion erronea"
        partido=input("A qué partido desea votar? A, B o C: ")
        if(partido=="A"):
            print("Usted ha votado al partido rojo.")
        elif(partido=="B"):
            print("Usted ha votado al partido verde")
        elif(partido=="C"):
            print("Usted ha votado al partido azul.")
        else: 
            print("Opción errónea.")
    elif(menu==7): #solicitamos al usuario una letra. Comprobamos que solo ha introducido una comparandola con 1. Comparamos si es una vocal con un if y su opción "or", y si es positivo, se muestra un mensaje.
        letra=input("Introduzca una letra: ")
        if(len(letra)!=1):
            print("No se puede realizar la operación.")
        else:
            if(letra=="a" or letra=="o" or letra=="i" or letra=="o" or letra=="u"):
                print("Es vocal.")
    elif(menu==8): #solicitamos al usuario y la mostramos 10 veces con un bucle for
        palabra=input("Introduzca una palabra, por favor: ")
        for i in range(10):
            print(palabra)
    elif(menu==9): #solicitamos al usuario su edad y mostramos todos los numeros a partir de 0 con un bucle for.
        num=input("Por favor, introduzca su edad: ")
        num=int(num)
        for i in range(1, (num+1)):
            print(i)
    elif(menu==10): #solicitamos al usuario un número, y repetimos tantas veces como valor tenga el número esta acción: cogemos el contador de iteraciones del for y lo dividimos entre 2. si el resultado no es 0, lo mostramos por pantalla.
        num=input("Por favor, introduzca un numero: ")
        num=int(num)
        for i in range(1, (num+1)):
            if(i%2 != 0):
                print(str(i)+", ", end="")
            print("")
    elif(menu==11): #solicitamos al usuario un número, y mostramos los numeros que hay del 0 a dicho numero al revés con la opción reversed del bucle for
        num=input("Por favor, introduzca un numero: ")
        num=int(num)
        for i in reversed(range(num)):
            print(i)
    elif(menu==12): #creamos la variable valido. siempre que valido sea false, preguntamos al usuario si quiere seguir con el programa. si responde "sí", el programa sigue, si responde otra cosa, la variable valido pasa a ser true
        valido=False
        while(valido!=True):
            print("Desea continuar con el programa?")
            respuesta=input("sí/no: ")
            if(respuesta=="sí"):
                valido=False
            else:
                valido=True
    elif(menu==13): #solicitamos al usuario un número y comprobamos que sea mayor que 2. Si esta condición se cumple, se va sumando y mostrando por pantalla "*" tantas veces como se haya introducido.
        valido=False
        triangulo=""
        while(valido!=True):
            num=input("Por favor, introduzca un numero: ")
            num=int(num)
            if(num<2):
                print("Pro favor, introduzca un número válido")
                valido=False
            else:
                valido=True
        for i in range(1, (num+1)):
            triangulo=triangulo+"*"
            print(triangulo)
    elif(menu==14): #se multiplica 10 veces por 10 el contador de iteraciones del for.
        for i in range(1, 11):
            print(i*10)
    elif(menu==15): #siempre que el usuario no escriba "salir", se va a recoger lo que escriba por pantalla y a mostrarlo acto seguido.
        print("Programa eco (salir para salir): ")
        valido=False
        while(valido!=True):
            eco=input()
            if(eco=="salir"):
                valido=True
            else: 
                valido=False
                print(eco)
    elif(menu==16): #se solicita al usuario una contraseña. se le vuelve a pedir. si no coinciden, se repite esta ultima accion.
        print("Introduzca una contraseña: ")
        psw=input()
        valido=False
        while(valido!=True):
            print("Repita su contraseña: ")
            psw2=input()
            if(psw==psw2):
                valido=True
            else: 
                valido=False
                print("Contraseña incorrecta")
    elif(menu==17): #solicitamos al usuario un número y comprobamos que sea mayor que 2. Si esta condición se cumple, se va sumando y mostrando por pantalla todos los números que no se puedan dividir entre 2, de manera inversa con la opción reversed del for.
        valido=False
        triangulo=""
        while(valido!=True):
            num=input("Por favor, introduzca un numero: ")
            num=int(num)
            if(num<2):
                print("Pro favor, introduzca un número válido")
                valido=False
            else:
                valido=True
        for i in range(1, (num+1)):
            if(i%2 != 0):
                triangulo=str(i)+" "+triangulo
                print(triangulo)
    elif(menu==18): #solicitamos al usuario la cantidad que desee ahorrar. Siempre que el total sea menor a la cantidad deseada, se solicita al usuario cuánto desea introducir y se comprueba que es mayor que 0.
        print("Introduzca la cantidad que desee ahorrar:")
        ahorro=input()
        ahorro=int(ahorro)
        total=0
        total=int(total)
        while(total<ahorro):
            valido=False
            while(valido!=True):
                print("Cuánto desea introducir?")
                dinero=input()
                dinero=int(dinero)
                if(dinero>0):
                    valido=True
                else:
                    print("Introduzca un número positivo, por favor")
                    valido=False
            total=total+int(dinero)
            print("Usted ha ahorrado: "+str(total))
        print("Programa de ahorro finalizado.")
    elif(menu==19): #solicitamos al usuario la cantidad que desee ahorrar. Siempre que el total sea menor a la cantidad deseada, se solicita al usuario cuánto desea introducir
        print("Introduzca la cantidad que desee ahorrar:")
        ahorro=input()
        ahorro=int(ahorro)
        total=0
        total=int(total)
        while(total<ahorro):
            print("Cuánto desea introducir?")
            dinero=input()
            dinero=int(dinero)
            total=total+int(dinero)
            print("Usted ha ahorrado: "+str(total))
        print("Programa de ahorro finalizado.")
    elif(menu==20): #se solicita al usuario una palabra, y se muestra letra por letra al revés con la opción reversed del for.
        palabra=input("Introduzca una palabra, por favor: ")
        for caracter in reversed(palabra):
            print(caracter)
    elif(menu==21): #se solicita al usuario una frase y una letra, y se compara cada letra de la frase con la introducida. Si es positivo, se suma +1 al contador. 
        frase=input("Introduzca una frase, por favor: ")
        letra=input("Introduzca una letra por favor.")
        total=0
        for i in frase:
            if(i==letra):
                total=total+1
        print("La letra "+letra+" se ha introducido "+str(total)+" veces.")
    elif(menu==22):
        truexit=True
