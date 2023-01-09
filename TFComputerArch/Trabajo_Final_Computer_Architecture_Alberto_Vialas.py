import random

entrada=[]
intermedio=[]
salida=[]

#Los dos tienen que ser true para que devuelva true
def _and(x,y,a,b):
    if x == 1 and y == 1 and a == 1 and b == 1:
        return 1
    else:
        return 0

#Si uno de los dos es true devuelve true
def _or(x,y,a,b):
    if x == 0 and y == 0 and a == 0 and b == 0:
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
def _nand(x,y,a,b):
    if x == 1 and y == 1 and a == 1 and b == 1:
        return 0
    else:
        return 1

#Es la negacion del operador OR
def _nor(x,y,a,b):
    if x == 0 and y == 0 and a == 0 and b == 0:
        return 1
    else:
        return 0 

#la salida es verdadera si las entradas no son iguales
def _xor(x,y,a,b):
    if x == y and y == a and a == b:
        return 0
    else:
        return 1
    
#Es la inversa de XOR
def _xnor(x,y,a,b):
    if x == y and y == a and a == b:
        return 1
    else:
        return 0


#Los dos tienen que ser true para que devuelva true
def _and2(x,y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0

#Si uno de los dos es true devuelve true
def _or2(x,y):
    if x == 0 and y == 0:
        return 0
    else:
        return 1

#Da una salida falsa solo si todas sus entradas son verdaderas
def _nand2(x,y):
    if x == 1 and y == 1:
        return 0
    else:
        return 1

#Es la negacion del operador OR
def _nor2(x,y):
    if x == 0 and y == 0:
        return 1
    else:
        return 0 

#la salida es verdadera si las entradas no son iguales
def _xor2(x,y):
    if x == y:
        return 0
    else:
        return 1
    
#Es la inversa de XOR
def _xnor2(x,y):
    if x == y:
        return 1
    else:
        return 0

#Los dos tienen que ser true para que devuelva true
def _and3(x,y,a):
    if x == 1 and y == 1 and a == 1:
        return 1
    else:
        return 0

#asignamos valores aleatorios para las entradas
def entrada(numero):
    entrada=[]
    for i in range(numero):
        aux=random.randrange(2)
        entrada.append(aux)
    return entrada

#asignamos valores aleatorios para las variables de control
def cont(numero):
    control=[]
    for i in range(numero):
        aux=random.randrange(2)
        control.append(aux)
    return control

#miramos qué puerta se abre y si es positiva o negativa
def multiplexor(input, contdec):
    for i in range(len(input)):
        if(contdec==i):
            if(input[i]==1):
                return 1
            else:
                return 0

#resolvemos la puerta lógica que se pasa al llamar la función
def asignapuerta(numero, opcion1, opcion2):
    if(numero==1):
        return(_and2(opcion1, opcion2))
    elif(numero==2):
        return(_or2(opcion1, opcion2))
    elif(numero==3):
        return(_nand2(opcion1, opcion2))
    elif(numero==4):
        return(_nor2(opcion1, opcion2))
    elif(numero==5):
        return(_xor2(opcion1, opcion2))
    elif(numero==6):
        return(_xnor2(opcion1, opcion2))


def ejercicios():
    #en esta función creamos un menú para elegir el ejercicio al que queremos acceder
    exitej=False
    while(exitej!=True):
        print("------------------------------------")
        print("------------Menú-puertas------------")
        print("------------------------------------")
        print("\n1- 1")
        print("2- 2")
        print("3- 3")
        print("4- 4")
        print("5- Salir.")
        opej=int(input("Por favor, introduzca el número del ejercicio que desee ver: "))

        #Comprobamos qué opción se ha escogido
        if(opej==1):
            print("")
            ej1()
        elif(opej==2):
            print("")
            ej2()
        elif(opej==3):
            print("")
            ej3()
        elif(opej==4):
            print("")
            ej4()
        elif(opej==5):
            print("")
            exitej=True
        else:
            print("Introduzca una opción válida!")

#aquí creamos un array de datos de entrada, comparamos qué puerta se ha abierto tras pasar el control a decimal y mostramos el resultado
def ej1():
    print("Bienvenido al multiplexor 8:1")
    intro=entrada(8)
    control=cont(3)
    contdec=(control[0]*2**2) + (control[1]*2**1) + (control[2]*2**0)
    solucion=multiplexor(intro, contdec)
    print("Abierta la puerta I"+str(contdec)+", resultado: "+str(solucion))

#creamos un array de datos de entrada
def ej2():
    print("Bienvenidos al multiplexor 16:1")
    intro=entrada(16)
    print(intro)
    #damos a elegir entre las dos opciones
    print("Desea la opción A (varios mux 2:1), o la opción B (varios mux 4:1)")
    opcion=input("")
    #si sale la opcion A, concatenamos varios mux de 2:1 para que la salida sea sólo 1 dígito
    if(opcion=="A"):
        print("Opción A:")
        intermedio=[]
        intermedio2=[]
        final=[]
        control=cont(1)
        contdec=control[0]*2**0
        for i in range(8):
            intermedio.append(multiplexor(intro, contdec))
            del intro[0]
            if(len(intro)>1):
                del intro[0]
            print(intermedio)
        control=cont(1)
        contdec=control[0]*2**0
        for i in range(4):
            intermedio2.append(multiplexor(intermedio, contdec))
            del intermedio[0]
            if(len(intermedio)>1):
                del intermedio[0]
            print(intermedio2)  
        control=cont(1)
        contdec=control[0]*2**0
        for i in range(2):
            final.append(multiplexor(intermedio2, contdec))
            del intermedio2[0]
            if(len(intermedio2)>1):
                del intermedio2[1]
            print(final) 
        control=cont(1)
        contdec=control[0]*2**0
        salida=multiplexor(final, contdec)
        print("La salida es: "+str(salida))
    #si sale la opcion B, concatenamos varios mux de 4:1 para que la salida sea sólo 1 dígito
    if(opcion=="B"):
        print("Opción B:")
        intermedio=[]
        control=cont(3)
        contdec=(control[0]*2**1)+(control[1]*2**0)
        for i in range(4):
            intermedio.append(multiplexor(intro, contdec))
            del intro[0]
            del intro[0]
            del intro[0]
            if(len(intro)>1):
                del intro[0]
            print(intermedio)  
        control=cont(3)
        contdec=(control[0]*2**1)+(control[1]*2**0)
        salida=multiplexor(intermedio, contdec)
        print("La salida es: "+str(salida))
        
#creamos un array de variables de control
def ej3():
    print("Bienvenidos al multiplexor 8:1 personalizable")
    intro=entrada(8)
    puerta=""
    intermedio=[]
    control=[]
    control.append(random.randrange(2))
    control.append(random.randrange(2))
    control.append(random.randrange(2))

    #elegimos qué puertas queremos
    for i in range(8):
        print("¿Qué puerta desea para la entrada "+str(i))
        puerta=int(input("1- and, 2- or, 3- nand, 4- nor, 5- xor, 6- xnor "))
        if(puerta==1):
            intermedio.append(_and(control[0], control[1], control[2], intro[i]))
        elif(puerta==2):
            intermedio.append(_or(control[0], control[1], control[2], intro[i]))
        elif(puerta==3):
            intermedio.append(_nand(control[0], control[1], control[2], intro[i]))
        elif(puerta==4):
            intermedio.append(_nor(control[0], control[1], control[2], intro[i]))
        elif(puerta==5):
            intermedio.append(_xor(control[0], control[1], control[2], intro[i]))
        elif(puerta==6):
            intermedio.append(_xnor(control[0], control[1], control[2], intro[i]))

    intermedio2=[]
    puerta2=[]
    puerta3=[]
    final=[]
    opcion1=""
    opcion2=""
    opcion3=""
    opcion4=""
    opcion5=""
    opcion6=""
    #elegimos que puertas queremos para el segundo grupo
    for i in range(4):
        print("¿Qué puerta desea para la entrada "+str(i)+" del segundo grupo?")
        puerta2.append(int(input("1- and, 2- or, 3- nand, 4- nor, 5- xor, 6- xnor ")))
    #asignamos cada valor a otro distinto y resolvemos la puerta
    for i in range(8):
        valido=False
        if(opcion1!=int(i) and opcion2!=int(i) and opcion3!=int(i) and opcion4!=int(i)):
            print("¿con qué posicion quiere emparejar la entrada I"+str(i)+" (0-7) ")
            if(opcion1==""):
                while(valido!=True):
                    opcion1=int(input(""))
                    if(opcion1>i):
                        intermedio2.append(asignapuerta(i, intermedio[i], opcion1))
                        valido=True
                    else:
                        print("Introduzca un valor nuevo!")
            elif(opcion2==""):
                while(valido!=True):
                    opcion2=int(input(""))
                    if(opcion2>i):
                        intermedio2.append(asignapuerta(i, intermedio[i], opcion2))
                        valido=True
                    else:
                        print("Introduzca un valor nuevo!")
            elif(opcion3==""):
                while(valido!=True):
                    opcion3=int(input(""))
                    if(opcion3>i):
                        intermedio2.append(asignapuerta(i, intermedio[i], opcion3))
                        valido=True
                    else:
                        print("Introduzca un valor nuevo!")
            elif(opcion4==""):
                while(valido!=True):
                    opcion4=int(input(""))
                    if(opcion4>i):
                        intermedio2.append(asignapuerta(i, intermedio[i], opcion4))
                        valido=True
                    else:
                        print("Introduzca un valor nuevo!")
    #elegimos que puertas queremos para el segundo grupo
    for i in range(2):
        print("¿Qué puerta desea para la entrada "+str(i)+" del segundo grupo?")
        puerta3.append(int(input("1- and, 2- or, 3- nand, 4- nor, 5- xor, 6- xnor ")))
    #asignamos cada valor a otro distinto y resolvemos la puerta
    for i in range(4):
        valido=False
        if(opcion5!=int(i) and opcion6!=int(i)):
            print("¿con qué posicion quiere emparejar la entrada I"+str(i)+" (0-3) ")
            if(opcion5==""):
                while(valido!=True):
                    opcion5=int(input(""))
                    if(opcion5>i):
                        final.append(asignapuerta(i, intermedio[i], opcion5))
                        valido=True
                    else:
                        print("Introduzca un valor nuevo!")
            elif(opcion6==""):
                while(valido!=True):
                    opcion6=int(input(""))
                    if(opcion6>i):
                        final.append(asignapuerta(i, intermedio[i], opcion6))
                        valido=True
                    else:
                        print("Introduzca un valor nuevo!")
    #hacemos la puerta final y mostramos el resultado
    solucion=_or2(final[0], final[1])
    print("La solucion del Mux es: "+int(solucion))

def ej4():
    print("Bienvenidos al demuxiplexor")
    intro=entrada(1)
    control1=cont(2)
    control2=cont(2)
    salida1=_and3(intro, control1, _not(control2))
    salida2=_and3(intro, _not(control1), control2)
    salida3=_and3(intro, control1, control2)
    salida4=_and3(intro, _not(control1), _not(control2))
    print("la solucion es: "+str(salida1)+", "+str(salida2)+", "+str(salida3)+", "+str(salida4))

ejercicios()