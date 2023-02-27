import heapq

def dijkstra(plano, inicio, final):
    # Inicializa las distancias a infinito para todos los vértices excepto el de inicio
    distanciav = {estaciones: float('infinity') for estaciones in plano}
    distanciav[inicio] = 0

    # Inicializa la cola de prioridad con el vértice de inicio
    cola = [(0, inicio)]

    # Inicializa un diccionario para almacenar los predecesores de cada estación
    previous = {estaciones: None for estaciones in plano}

    # Mientras la cola de prioridad no esté vacía
    while(colavacia(cola)==False):  
        # Toma el vértice con la distancia mínima en la cola
        (dist, estacionactual) = heapq.heappop(cola)

        # Si se ha llegado al vértice destino, detén el bucle
        if estacionactual == final:
            break

        # Revisa todos los vecinos del vértice actual
        for vecino, recorrido in plano[estacionactual].items():
            # Calcula la distancia a través de este vecino
            distancia = dist + recorrido

            # Si esta distancia es menor que la distancia actual al vecino, actualiza la distancia
            if distancia < distanciav[vecino]:
                distanciav[vecino] = distancia
                previous[vecino] = estacionactual
                # Agrega el vecino a la cola de prioridad
                heapq.heappush(cola, (distancia, vecino))

    # Construye la ruta más corta al seguir los predecesores desde el vértice destino hasta el inicio
    rutadij, estacionactual = [], final
    while estacionactual != inicio:
        rutadij.append(estacionactual)
        estacionactual = previous[estacionactual]
    rutadij.append(inicio)

    # Devuelve la distancia mínima y la ruta más corta
    return distanciav[final], rutadij[::-1]

# Comprueba si la cola está llena o vacía
def colavacia(cola):
    if(cola==[]):
        return True
    else:
        return False


# Grafo con el laberinto especificado 
grafo = {
            "a": {"b": 2, "c": 5},
            "b": {"a": 2, "c": 1, "d": 8},
            "c": {"a": 5, "b": 1, "d": 6},
            "d": {"b": 8, "c": 6}
        }


# Inicio del programa
inicial = "a"
final = "d"
distancia, ruta = dijkstra(grafo, inicial, final)
rutafinal=""
for i in range(len(ruta)):
    rutafinal=rutafinal+str(ruta[i])+"->"
print("La distancia mínima requerida para el trayecto es de "+str(distancia)+", para la cual hay que seguir la siguiente ruta: "+rutafinal[:-2])