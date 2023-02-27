import heapq

def matriz(graph):
    vertices = list(graph.keys())
    N = len(vertices)

    # Inicializar la matriz con ceros
    adj_matrix = [[0 for _ in range(N)] for _ in range(N)]

    # Recorrer el grafo y asignar el peso de cada arista a la posición correspondiente en la matriz
    for i in range(N):
        for j in range(N):
            if vertices[i] in graph and vertices[j] in graph[vertices[i]]:
                adj_matrix[i][j] = graph[vertices[i]][vertices[j]]

    # Imprimir la matriz de adyacencia
    for row in adj_matrix:
        print(row)
    
    return adj_matrix

def dijkstra(matriz_ady, inicio, final):
    # Inicializa las distancias a infinito para todos los vértices excepto el de inicio
    distanciav = [float('infinity')] * len(matriz_ady)
    distanciav[inicio] = 0

    # Inicializa la cola de prioridad con el vértice de inicio
    cola = [(0, inicio)]

    # Inicializa un diccionario para almacenar los predecesores de cada estación
    previous = [None] * len(matriz_ady)

    # Mientras la cola de prioridad no esté vacía
    while cola:
        # Toma el vértice con la distancia mínima en la cola
        (dist, nodoactual) = heapq.heappop(cola)

        # Si se ha llegado al vértice destino, detén el bucle
        if nodoactual == final:
            break

        # Revisa todos los vecinos del vértice actual
        vecinos = []
        for i in range(len(matriz_ady)):
            if matriz_ady[nodoactual][i] > 0:
                vecinos.append(i)

        for vecino in vecinos:
            # Calcula la distancia a través de este vecino
            distancia = dist + matriz_ady[nodoactual][vecino]

            # Si esta distancia es menor que la distancia actual al vecino, actualiza la distancia
            if distancia < distanciav[vecino]:
                distanciav[vecino] = distancia
                previous[vecino] = nodoactual
                # Agrega el vecino a la cola de prioridad
                heapq.heappush(cola, (distancia, vecino))

    # Construye la ruta más corta al seguir los predecesores desde el vértice destino hasta el inicio
    rutadij, nodoactual = [], final
    while nodoactual != inicio:
        rutadij.append(nodoactual)
        nodoactual = previous[nodoactual]
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
inicial = 0
final = 3
laberinto = matriz(grafo)
distancia, ruta = dijkstra(laberinto, inicial, final)
rutafinal=""
for i in range(len(ruta)):
    rutafinal=rutafinal+str(ruta[i])+"->"
print("La distancia mínima requerida para el trayecto es de "+str(distancia)+", para la cual hay que seguir la siguiente ruta: "+rutafinal[:-2])