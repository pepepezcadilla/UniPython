import heapq


def dijkstra(plano, inicio, final):
    # Inicializa las distancias a infinito para todos los vértices excepto el de inicio
    distanciav = {vertex: float('infinity') for vertex in plano}
    distanciav[inicio] = 0

    # Inicializa la cola de prioridad con el vértice de inicio
    cola = [(0, inicio)]

    # Inicializa un diccionario para almacenar los predecesores de cada vértice
    previous = {vertex: None for vertex in plano}

    # Mientras la cola de prioridad no esté vacía
    while(colavacia(cola)==False):  
        # Toma el vértice con la distancia mínima en la cola
        (dist, current) = heapq.heappop(cola)

        # Si se ha llegado al vértice destino, detén el bucle
        if current == final:
            break

        # Revisa todos los vecinos del vértice actual
        for neighbor, weight in plano[current].items():
            # Calcula la distancia a través de este vecino
            distancia = dist + weight

            # Si esta distancia es menor que la distancia actual al vecino, actualiza la distancia
            if distancia < distanciav[neighbor]:
                distanciav[neighbor] = distancia
                previous[neighbor] = current
                # Agrega el vecino a la cola de prioridad
                heapq.heappush(cola, (distancia, neighbor))

    # Construye la ruta más corta al seguir los predecesores desde el vértice destino hasta el inicio
    path, current = [], final
    while current != inicio:
        path.append(current)
        current = previous[current]
    path.append(inicio)

    # Devuelve la distancia mínima y la ruta más corta
    return distanciav[final], path[::-1]


def colavacia(cola):
    if(cola==[]):
        return True
    else:
        return False


grafo = {
    'Kings Cross St. Pancras': {'Euston': 1, 'Angel': 2},
    'Euston': {'Kings Cross St. Pancras': 1, 'Warren Street': 1},
    'Warren Street': {'Euston': 1, 'Goodge Street': 1},
    'Goodge Street': {'Warren Street': 1, 'Tottenham Court Road': 1},
    'Tottenham Court Road': {'Goodge Street': 1, 'Holborn': 1, 'Leicester Square': 2},
    'Holborn': {'Tottenham Court Road': 1, 'Chancery Lane': 1},
    'Chancery Lane': {'Holborn': 1, 'St. Pauls': 1},
    'St. Pauls': {'Chancery Lane': 1},
    'Leicester Square': {'Tottenham Court Road': 2, 'Covent Garden': 1},
    'Covent Garden': {'Leicester Square': 1, 'Holborn': 2},
    'Angel': {'Kings Cross St. Pancras': 2, 'Old Street': 2},
    'Old Street': {'Angel': 2, 'Moorgate': 1},
    'Moorgate': {'Old Street': 1, 'Liverpool Street': 1},
    'Liverpool Street': {'Moorgate': 1},
}

distancia, ruta = dijkstra(grafo, "Euston", "Moorgate")
rutafinal=""
for i in range(len(ruta)):
    rutafinal=rutafinal+str(ruta[i])+"->"
print("La distancia mínima requerida para el trayecto es de "+str(distancia)+", para la cual hay que seguir la siguiente ruta: "+rutafinal[:-2])