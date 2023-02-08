#Se les asigna pista en función de la posición en la que llegan al aeropuerto (en realidad es según el orden en el que están en el fichero, siendo el sentido desde la posición de arriba de fichero hacia abajo).
#Los vuelos con prioridad deberán pasar directamente al inicio de la lista, en el mismo orden en el que estaban en el fichero.
#Pistas:

#Hay tres pistas:
#P1 y P2 para los vuelos normales.
#P3: para los vuelos con prioridad. Si no hay vuelos con prioridad, se podrá usar también como pista de aterrizaje para los vuelos de prioridad normal.
#Especificaciones:

#Los vuelos que han aterrizado deberán ir grabándose en orden en un fichero de salida llamado "aterrizados.txt", donde se indica qué vuelo (en el orden correcto) en qué pista ha aterrizado

#Se deberán implementar con pilas y colas que a su vez deberán estar implementadas con listas enlazadas. Se deja a la estrategia del usuario utilizarla mediante listas enlazadas simples, dobles, circulares, etc.

#Se recomienda no usar el .pop, .insert, .append, etc. Y se prohíbe utilizar cualquier librería salvo para visualizar el contenido/posición de los vuelos en formato controlador aéreo real.

#Se deberán utilizar las funciones apilar,encolar,colavacía,colallena,pilallena,pilavacía,desapilar o desencolar según la estrategia que se utilice. Se podrán añadir a estas tantas funciones como se consideren necesarias.


def escribevuelos(vuelo, prioridad):
    with open("vuelos_in.txt", "a") as fichero:
        fichero.write(vuelo + prioridad + "\n")
    fichero.close

def vuelosiniciales():
    escribevuelos("MAD1234", "p")
    escribevuelos("CON6666", "p")
    escribevuelos("MOS8642", "n")
    escribevuelos("TOR2000", "n")
    escribevuelos("VIE6001", "n")
    escribevuelos("LON1130", "p")
    escribevuelos("IBI3478", "n")
    escribevuelos("BEI5524", "n")
    escribevuelos("AMS9961", "p")
    escribevuelos("JAV8346", "n")


vuelosiniciales()
