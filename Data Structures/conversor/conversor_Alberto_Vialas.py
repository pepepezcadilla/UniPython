#Creamos el diccionario
diccionario = {   
    }

#Creamos el menú para elegir el tipo de estructura
def tipos():
    exit=False
    while(exit!=True):
        print("------------------------------------")
        print("-----------Menú-tipos---------------")
        print("------------------------------------")
        print("\n1- Diccionarios")
        print("2- Array")
        print("3- Tuplas")
        print("4- Sin estructuras")
        print("5- Salir")
        opcion=int(input("Por favor, introduzca la opcion deseada: "))

        if(opcion==1):
            menu(1)
        elif(opcion==2):
            menu(2)
        elif(opcion==3):
            menu(3)
        elif(opcion==4):
            menu(4)
        elif(opcion==5):
            exit=True
        else:
            print("Introduzca un número válido!")

#creamos el menu principal
def menu(tipo):
    exit=False
    while(exit!=True):
        print("------------------------------------")
        print("-----------Menú-principal-----------")
        print("------------------------------------")
        print("\n1- Introducir datos")
        print("2- Mostrar datos")
        print("3- Salir")
        opcion=int(input("Por favor, introduzca la opcion deseada: "))

        #Comprobamos la opción elegida y el tipo de estructura escogida, y llamamos a las funciones.
        if(opcion==1):
            if(tipo==1):
                introdic()
            elif(tipo==2):
                valores=introar()
            elif(tipo==3):
                valorestup=introtup()
            elif(tipo==4):
                name=nombre()
                ape=apellido()
                age=edad()
                gen=genero()
                papa=padre1()
                mama=padre2()
        elif(opcion==2):
            if(tipo==1):
                muestradic()
            elif(tipo==2):
                muestrar(valores)
            elif(tipo==3):
                muestrtup(valorestup)
            elif(tipo==4):
                muestraestr(name, ape, age, gen, papa, mama)
        elif(opcion==3):
            exit=True
        else:
            print("Introduzca un número válido!")

#Rellenamos el diccionario con los inputs.
def introdic():
    valido=False
    while(valido!=True):    
        print("Bienvenido a los diccionarios, por favor, introduzca su nombre: ")
        nombre=input()
        if(nombre!=""):
            diccionario["Nombre"]=nombre
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su(s) apellido(s): ")
        apellido=input()
        if(apellido!=""):
            diccionario["Apellido"]=apellido
            valido=True
        else:
            print("Introduzca un apellido válido!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su edad: ")
        edad=int(input())
        if(edad!="" and edad<100):
            #llamamos a la funcion para transcribir la edad
            diccionario["Edad"]=stredad(edad)
            valido=True
        else:
            print("Introduzca una edad válida!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su género: ")
        genero=input()
        if(genero!=""):
            diccionario["Genero"]=genero
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False     
    print("Introduzca el nombre de sus padres: ")
    padres=[]
    while(valido!=True):    
        progenitor1=input("Padre(o madre) ")
        if(progenitor1!=""):
            padres.append(progenitor1)
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False
    while(valido!=True):
        progenitor2=input("Madre(o padre) ")
        if(progenitor2!=""):
            padres.append(progenitor2)
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False
    diccionario["Padres"]=padres

#mostramos el interior del diccionario
def muestradic():
    padre1=diccionario["Padres"][0]
    padre2=diccionario["Padres"][1]
    print("Mi nombre es "+diccionario["Nombre"]+" "+diccionario["Apellido"]+", tengo "+diccionario["Edad"]+" años y mis padres son "+padre1+" y "+padre2)


#-----------------------------------------------------------------Arrays------------------------------------------------

#Rellenamos el array con los inputs.
def introar():
    valores=[]
    valido=False
    while(valido!=True):    
        print("Bienvenido a los array, por favor, introduzca su nombre: ")
        nombre=input()
        if(nombre!=""):
            valores.append(nombre)
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su(s) apellido(s): ")
        apellido=input()
        if(apellido!=""):
            valores.append(apellido)
            valido=True
        else:
            print("Introduzca un apellido válido!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su edad: ")
        edad=int(input())
        if(edad!="" and edad<100):
            #llamamos a la funcion para transcribir la edad
            valores.append(stredad(edad))
            valido=True
        else:
            print("Introduzca una edad válida!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su género: ")
        genero=input()
        if(genero!=""):
            valores.append(genero)
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False     
    print("Introduzca el nombre de sus padres: ")
    padres=[]
    while(valido!=True):    
        progenitor1=input("Padre(o madre) ")
        if(progenitor1!=""):
            padres.append(progenitor1)
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False
    while(valido!=True):
        progenitor2=input("Madre(o padre) ")
        if(progenitor2!=""):
            padres.append(progenitor2)
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False
    valores.append(padres)
    return valores

#mostramos el interior del array
def muestrar(valores):
    print("Mi nombre es "+valores[0]+" "+valores[1]+", tengo "+valores[2]+" años y mis padres son "+valores[4][0]+" y "+valores[4][1])


#-----------------------------------------------------------------Tuplas------------------------------------------------

#Rellenamos la tupla con los inputs.
def introtup():
    valido=False
    while(valido!=True):    
        print("Bienvenido a las tuplas, por favor, introduzca su nombre: ")
        nombre=input()
        if(nombre!=""):
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su(s) apellido(s): ")
        apellido=input()
        if(apellido!=""):
            valido=True
        else:
            print("Introduzca un apellido válido!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su edad: ")
        edad=int(input())
        if(edad!="" and edad<100):
            #llamamos a la funcion para transcribir la edad
            edad=stredad(edad)
            valido=True
        else:
            print("Introduzca una edad válida!")
            valido=False

    valido=False
    while(valido!=True):    
        print("Introduzca su género: ")
        genero=input()
        if(genero!=""):
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False     
    print("Introduzca el nombre de sus padres: ")
    while(valido!=True):    
        progenitor1=input("Padre(o madre) ")
        if(progenitor1!=""):
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False

    valido=False
    while(valido!=True):
        progenitor2=input("Madre(o padre) ")
        if(progenitor2!=""):
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False
    valores=(nombre, apellido, edad, genero, progenitor1, progenitor2)
    return valores

#mostramos el interior de la tupla
def muestrtup(valores):
    print("Mi nombre es "+valores[0]+" "+valores[1]+", tengo "+valores[2]+" años y mis padres son "+valores[4]+" y "+valores[5])


#-----------------------------------------------------------------Sin Estructura------------------------------------------------

#Varias funciones para ir asignando y retornando los valores nombre, apellidos, edad, genero, padre1 y padre2
def nombre():
    valido=False
    while(valido!=True):    
        print("Bienvenido a los valores sin estructura, por favor, introduzca su nombre: ")
        nombre=input()
        if(nombre!=""):
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False
    return nombre

def apellido():
    valido=False
    while(valido!=True):    
        print("Introduzca su(s) apellido(s): ")
        apellido=input()
        if(apellido!=""):
            valido=True
        else:
            print("Introduzca un apellido válido!")
            valido=False
    return apellido

def edad():
    valido=False
    while(valido!=True):    
        print("Introduzca su edad: ")
        edad=int(input())
        if(edad!="" and edad<100):
            #llamamos a la funcion para transcribir la edad
            edad=estr(edad)
            valido=True
        else:
            print("Introduzca una edad válida!")
            valido=False
    return edad

def genero():
    valido=False
    while(valido!=True):    
        print("Introduzca su género: ")
        genero=input()
        if(genero!=""):
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False
    return genero

def padre1():
    valido=False     
    print("Introduzca el nombre de sus padres: ")
    while(valido!=True):    
        progenitor1=input("Padre(o madre) ")
        if(progenitor1!=""):
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False
    return progenitor1

def padre2():
    valido=False
    while(valido!=True):
        progenitor2=input("Madre(o padre) ")
        if(progenitor2!=""):
            valido=True
        else:
            print("Introduzca un nombre válido!")
            valido=False
    return progenitor2

#mostramos el interior de las variables
def muestraestr(nombre, apellido, edad, genero, padre1, padre2):
    print("Mi nombre es "+nombre+" "+apellido+", tengo "+edad+" años y mis padres son "+padre1+" y "+padre2)


#-----------------------------------------------------------------Funciones------------------------------------------------

#Transcribimos los numeros 1-99 sin usar arrays
def estr(edad):
    match edad:
        case 1:
            return "uno"
        case 2:
            return "dos"
        case 3:
            return "tres"
        case 4:
            return "cuatro"
        case 5:
            return "cinco"
        case 6:
            return "seis"
        case 7:
            return "siete"
        case 8:
            return "ocho"
        case 9:
            return "nueve"
        case 10:
            return "diez"
        case 11:
            return "once"
        case 12:
            return "doce"
        case 13:
            return "trece"
        case 14:
            return "catorce"
        case 15:
            return "quince"
        case 16:
            return "dieciseis"
        case 17:
            return "diecisiete"
        case 18:
            return "dieciocho"
        case 19:
            return "diecinueve"
        case 20:
            return "veinte"
        case 21:
            return "veintiuno"
        case 22:
            return "veintidos"
        case 23:
            return "veintitres"
        case 24:
            return "veinticuatro"
        case 25:
            return "veinticinco"
        case 26:
            return "veintiseis"
        case 27:
            return "veintisiete"
        case 28:
            return "veintiocho"
        case 29:
            return "veintinueve"
        case 30:
            return "treinta"
        case 31:
            return "treinta y uno"
        case 32:
            return "treinta y dos"
        case 33:
            return "treinta y tres"
        case 34:
            return "treinta y cuatro"
        case 35:
            return "treinta y cinco"
        case 36:
            return "treinta y seis"
        case 37:
            return "treinta y siete"
        case 38:
            return "treinta y ocho"
        case 39:
            return "treinta y nueve"
        case 40:
            return "cuarenta"
        case 41:
            return "cuarenta y uno"
        case 42:
            return "cuarenta y dos"
        case 43:
            return "cuarenta y tres"
        case 44:
            return "cuarenta y cuatro"
        case 45:
            return "cuarenta y cinco"
        case 46:
            return "cuarenta y seis"
        case 47:
            return "cuarenta y siete"
        case 48:
            return "cuarenta y ocho"
        case 49:
            return "cuarenta y nueve"
        case 50:
            return "cincuenta"
        case 51:
            return "cincuenta y uno"
        case 52:
            return "cincuenta y dos"
        case 53:
            return "cincuenta y tres"
        case 54:
            return "cincuenta y cuatro"
        case 55:
            return "cincuenta y cinco"
        case 56:
            return "cincuenta y seis"
        case 57:
            return "cincuenta y siete"
        case 58:
            return "cincuenta y ocho"
        case 59:
            return "cincuenta y nueve"
        case 60:
            return "sesenta"
        case 61:
            return "sesenta y uno"
        case 62:
            return "sesenta y dos"
        case 63:
            return "sesenta y tres"
        case 64:
            return "sesenta y cuatro"
        case 65:
            return "sesenta y cinco"
        case 66:
            return "sesenta y seis"
        case 67:
            return "sesenta y siete"
        case 68:
            return "sesenta y ocho"
        case 69:
            return "sesenta y nueve"
        case 70:
            return "setenta"
        case 71:
            return "setenta y uno"
        case 72:
            return "setenta y dos"
        case 73:
            return "setenta y tres"
        case 74:
            return "setenta y cuatro"
        case 75:
            return "setenta y cinco"
        case 76:
            return "setenta y seis"
        case 77:
            return "setenta y siete"
        case 78:
            return "setenta y ocho"
        case 79:
            return "setenta y nueve"
        case 80:
            return "ochenta"
        case 81:
            return "ochenta y uno"
        case 82:
            return "ochenta y dos"
        case 83:
            return "ochenta y tres"
        case 84:
            return "ochenta y cuatro"
        case 85:
            return "ochenta y cinco"
        case 86:
            return "ochenta y seis"
        case 87:
            return "ochenta y siete"
        case 88:
            return "ochenta y ocho"
        case 89:
            return "ochenta y nueve"
        case 90:
            return "noventa"
        case 91:
            return "noventa y uno"
        case 92:
            return "noventa y dos"
        case 93:
            return "noventa y tres"
        case 94:
            return "noventa y cuatro"
        case 95:
            return "noventa y cinco"
        case 96:
            return "noventa y seis"
        case 97:
            return "noventa y siete"
        case 98:
            return "noventa y ocho"
        case 99:
            return "noventa y nueve"

#Separamos la edad por números y las asignamos, si es menor que 10, llamamos a la funcion unidades, si es entre 10 y 19, lo transcribimos, y si es superior, llamamos a la funcion decenas
def stredad(edad):
    splited=list(str(edad))
    result=""
    
    if(len(splited)==1):
        result=unidades(edad)
    elif(len(splited)==2):
        if(int(splited[0])==1):
            if(int(splited[1])==0):
                result="diez"
            elif(int(splited[1])==1):
                result="once"
            elif(int(splited[1])==2):
                result="doce"
            elif(int(splited[1])==3):
                result="trece"
            elif(int(splited[1])==4):
                result="catorce"
            elif(int(splited[1])==5):
                result="quince"
            elif(int(splited[1])==6):
                result="dieciseis"
            elif(int(splited[1])==7):
                result="diecisiete"
            elif(int(splited[1])==8):
                result="dieciocho"
            elif(int(splited[1])==9):
                result="diecinueve"
        else:
            result=decenas(splited[0], splited[1])

    return result

#Transcribimos las unidades de la edad 
def unidades(edad):
    if(edad==1):
        return "uno"
    elif(edad==2):
        return "dos"
    elif(edad==3):
        return "tres"
    elif(edad==4):
        return "cuatro"
    elif(edad==5):
        return "cinco"
    elif(edad==6):
        return "seis"
    elif(edad==7):
        return "siete"
    elif(edad==8):
        return "ocho"
    elif(edad==9):
        return "nueve"

#Transcribimos las decenas, llamando a la funcion unidades.
def decenas(deca, uni):
    decena=int(deca)
    unidad=int(uni)
    if(decena==2):
        if(unidad==0):
            return "veinte"
        else:
            return "veinti"+unidades(unidad)
    elif(decena==3):
        if(unidad==0):
            return "treinta"
        else:
            return "treinta y "+unidades(unidad)
    elif(decena==4):
        if(unidad==0):
            return "cuarenta"
        else:
            return "cuarenta y "+unidades(unidad)
    elif(decena==5):
        if(unidad==0):
            return "cincuenta"
        else:
            return "cincuenta y "+unidades(unidad)
    elif(decena==6):
        if(unidad==0):
            return "sesenta"
        else:
            return "sesenta y "+unidades(unidad)
    elif(decena==7):
        if(unidad==0):
            return "setenta"
        else:
            return "setenta y "+unidades(unidad)
    elif(decena==8):
        if(unidad==0):
            return "ochenta"
        else:
            return "ochenta y "+unidades(unidad)
    elif(decena==9):
        if(unidad==0):
            return "noventa"
        else:
            return "noventa y "+unidades(unidad)

#Comenzamos el programa
tipos()