#Importamos la librería time para simular el tráfico de aviones (sólo estética)
import time

#Creamos la clase Cola, para almacenar los vuelos que llegan.
class Cola:
    #Creamos el método constructor
    def __init__(self):
        self.items=[]

    #Creamos el método para añadir elementos a la cola
    def encolar(self, vuelo):
        self.items.append(vuelo)

    #Creamos el método para elominar elementos de la cola, salta un error si ya está vacía
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    #Creamos el método para vaciar la cola
    def vaciarcola(self):
        self.items=[]
    
    #Creamos el método para comprobar si la cola está vacía o no
    def colavacia(self):
        if(self.items==[]):
            return True
        else:
            return False


#Creamos la función para escribir el fichero con los vuelos que entran, también llamamos a la función para leer el fichero y guardarlo en una lista.
def escribevuelos(vuelo, prioridad, lista):
    with open("vuelos_in.txt", "a") as fichero:
        fichero.write(vuelo + prioridad + "\n")
    fichero.close
    lista=leefichero("vuelos_in.txt")
    return lista


#Creamos la función que escribe los vuelos que van aterrizando
def escribeaterr(vuelo):
    with open("aterrizados.txt", "a")as fichero:
        fichero.write(vuelo+"\n")
    fichero.close


#Creamos una lista con 10 vuelos
def vuelosiniciales(lista):
    escribevuelos("MAD1234", "n", lista)
    escribevuelos("CON6666", "p", lista)
    escribevuelos("MOS8642", "n", lista)
    escribevuelos("TOR2000", "n", lista)
    escribevuelos("VIE6001", "n", lista)
    escribevuelos("LON1130", "p", lista)
    escribevuelos("IBI3478", "n", lista)
    escribevuelos("BEI5524", "n", lista)
    escribevuelos("AMS9961", "n", lista)
    escribevuelos("JAV8346", "n", lista)


#Creamos una función para leer el fichero donde están almacenados los vuelos y los pasa a una lista
def leefichero(nombrefichero):
    with open(nombrefichero, "r")as fichero:
        lineas=fichero.readlines()
        for i in range(len(lineas)):
            splieado = lineas[i].split("\n")
            lineas[i] = splieado[0]
        fichero.close
        return lineas


#Creamos la función que llena dos colas, diferenciando entre vuelos prioritarios y no prioritarios
def llenacola(lista, cola1, cola2):
    cola1.vaciarcola()
    cola2.vaciarcola()
    for i in range(len(lista)):
        if(lista[i][-1:]=="p"):
            cola1.encolar(lista[i])
    for i in range(len(lista)):
        if(lista[i][-1:]=="n"):
            cola2.encolar(lista[i])
    return(cola1, cola2)


#Creamos una función para asignar cada vuelo a una pista, y vamos eliminandolos de las colas
def asignapista(prio, noprio):
    pista1=""
    pista2=""
    pista3=""
    while(prio.colavacia()!=True or noprio.colavacia!=True):
        if(noprio.colavacia()==False):
            pista1 = noprio.desencolar()
            print("Ha aterrizado el vuelo "+str(pista1)+" en la pista 1")
            escribeaterr(pista1)
            time.sleep(0.5)

        if(noprio.colavacia()==False):
            pista2 = noprio.desencolar()
            print("Ha aterrizado el vuelo "+str(pista2)+" en la pista 2")
            escribeaterr(pista2)
            time.sleep(0.5)

        if(prio.colavacia()==False):
            pista3 = prio.desencolar()
            print("Ha aterrizado el vuelo "+str(pista3)+" en la pista 3")
            escribeaterr(pista3)
            time.sleep(0.5)
        elif(noprio.colavacia()==False):
            pista3 = noprio.desencolar()
            print("Ha aterrizado el vuelo "+str(pista3)+" en la pista 3")
            escribeaterr(pista3)
            time.sleep(0.5)

        time.sleep(1)

#Inicio del programa
colaprioritarios = Cola()
colanoprioritarios = Cola()
listavuelos = []
listavuelos = vuelosiniciales(listavuelos)
listavuelos = escribevuelos("SPT0666", "n", listavuelos)
colaprioritarios, colanoprioritarios = llenacola(listavuelos, colaprioritarios, colanoprioritarios)
listavuelos = escribevuelos("MOS9999", "n", listavuelos)
colaprioritarios, colanoprioritarios = llenacola(listavuelos, colaprioritarios, colanoprioritarios)
asignapista(colaprioritarios, colanoprioritarios)

