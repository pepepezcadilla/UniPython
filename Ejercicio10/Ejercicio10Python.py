contador=3
correct=False
exit=False
opcion2=False
cont=""
cont2=""
while(exit!=True): #Aquí comprobamos que el usuario quiere seguir en el programa
    if(opcion2!=True): #Aquí comprobamos si el usuario ha elegido la opción 2
        print("Indique una opción:\n1- Introducir contraseña\n2- Cambiar contraseña\n3- Exit")
        print("Opción deseada: ", end="")
        option=input()
    if(option=="1"): #opción 1
        contok=False
        if(cont!=""): #Comprobamos si ya había una contraseña anteriormente
            print("Ya se ha introducido una contraseña anteriormente.")
        else:
            opcion2=False
            while(contok!=True): #Pedimos la contraseña y comprobamos si está vacía
                print("Introduzca una contraseña por favor:")
                cont=str(input("Contraseña: "))
                if(cont==""):
                    print("Contraseña vacía.")
                else:
                    contok=True
            print("Repita la contraseña por favor:")
            cont2=str(input("Contraseña: "))
            while(correct!=True): #Comprobamos que las contraseñas son iguales, y si no, pedimos la segunda otra vez, máximo 3 veces
                if(cont==cont2):
                    correct=True
                else:
                    if(contador>0):
                        contador=contador-1
                        print("Contraseñas no coinciden, introduzca de nuevo la contraseña por favor:")
                        cont2=str(input("Contraseña: "))
                    else: #Salimos de la opción 1, al haberse acabado los intentos.
                        print("Demasiados intentos fallidos.")
                        cont=""
                        cont2=""
                        break
    if(option=="2"): #Opción 2
        if(cont==""): #Comprobamos si hay alguna contraseña que cambiar.
            print("Contraseña vacía, por favor, introduzca una.")
        else: #Vaciamos las contraseñas y enviamos el programa a la opción 1
            opcion2=True
            cont=""
            cont2=""
            option="1"
    if(option=="3"): #Preguntamos si queremos salir, y cerramos el programa.
        print("¿Desea salir? yes/no ", end="")
        salir=input()
        if(salir=="yes"):
            exit=True