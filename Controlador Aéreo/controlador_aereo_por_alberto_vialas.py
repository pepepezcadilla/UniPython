import time

class Cola:

    def __init__(self):
        self.items=[]

    def encolar(self, vuelo):
        self.items.append(vuelo)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def vaciarcola(self):
        self.items=[]
    
    def colavacia(self):
        if(self.items==[]):
            return True
        else:
            return False



def escribevuelos(vuelo, prioridad, lista):
    with open("vuelos_in.txt", "a") as fichero:
        fichero.write(vuelo + prioridad + "\n")
    fichero.close
    lista=leefichero("vuelos_in.txt")
    return lista


def escribeaterr(vuelo):
    with open("aterrizajes.txt", "a")as fichero:
        fichero.write(vuelo+"\n")
    fichero.close


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


def leefichero(nombrefichero):
    with open(nombrefichero, "r")as fichero:
        lineas=fichero.readlines()
        for i in range(len(lineas)):
            splieado = lineas[i].split("\n")
            lineas[i] = splieado[0]
        fichero.close
        return lineas


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


colaprioritarios = Cola()
colanoprioritarios = Cola()
listavuelos = []
listavuelos = vuelosiniciales(listavuelos)
listavuelos = escribevuelos("SPT0666", "n", listavuelos)
colaprioritarios, colanoprioritarios = llenacola(listavuelos, colaprioritarios, colanoprioritarios)
listavuelos = escribevuelos("MOS9999", "n", listavuelos)
colaprioritarios, colanoprioritarios = llenacola(listavuelos, colaprioritarios, colanoprioritarios)
asignapista(colaprioritarios, colanoprioritarios)

