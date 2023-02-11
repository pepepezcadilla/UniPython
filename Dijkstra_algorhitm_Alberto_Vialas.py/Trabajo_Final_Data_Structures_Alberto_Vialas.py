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


def colavacia(cola):
    if(cola==[]):
        return True
    else:
        return False


grafo = {
            "amersham": {"baker street": 9},
            "chorleywoood": {"amersham": 1, "wembley park": 10},
            "uxbridge": {"rayners lane": 6},
            "rayners lane": {"uxbridge": 6, "ealing common": 7, "wembley park": 5},
            "wembley park": {"chorleywoood": 10, "finchley road": 1, "rayners lane": 5, "stanmore": 4, "west hampstead": 5},
            "finchley road": {"wembley park": 1, "baker street": 1, "west hampstead": 1},
            "baker street": {"finchley road": 2, "kings cross": 3, "paddington": 3, "oxford circus": 2, "edgware road": 1, "bond street": 1},
            "kings cross": {"baker street": 3, "moortage": 3, "holborn": 2, "finsbury park": 4, "euston": 1, "highbury & islington": 1},
            "moortage": {"kings cross": 3, "liverpool street": 1, "bank": 1},
            "liverpool street": {"moortage": 1, "aldgate": 1, "bank": 1, "mile end": 2, "aldgate east": 1, "tower hill": 1},
            "aldgate": {"liverpool street": 1},
            "ealing common": {"rayners lane": 7, "acton town": 1, "ealing broadway": 1},
            "acton town": {"ealing common": 1, "hammersmith": 5, "terminal": 10},
            "terminal": {"acton town": 10},
            "hammersmith": {"acton town": 5, "barons court": 1, "richmond": 6, "paddington": 8},
            "barons court": {"hammersmith": 1, "earls court": 2},
            "earls court": {"barons court": 2, "gloucester road": 1, "wimbledon": 8, "olympia": 1, "notting hill gate": 2},
            "gloucester road": {"earls court": 1, "south kensington": 1, "notting hill gate": 2},
            "south kensington": {"gloucester road": 1, "green park": 3, "victoria": 1},
            "green park": {"south kensington": 3, "piccadilly circus": 1, "oxford circus": 1, "victoria": 1,"bond street": 1, "westminster": 1},
            "piccadilly circus": {"green park": 1, "leicester square": 1, "oxford circus": 1, "charing cross": 1},
            "leicester square": {"piccadilly circus": 1, "holborn": 2, "tottenham court road": 1, "charing cross": 1},
            "holborn": {"leicester square": 2, "kings cross": 2, "tottenham court road": 1, "bank": 3},
            "finsbury park": {"kings cross": 4, "cock fosters": 8, "walthamstow central": 4, "highbury & islington": 1},
            "cock fosters": {"finsbury park": 8},
            "high barnet": {"camden town": 10},
            "edware": {"camden town": 9},
            "camden town": {"high barnet": 10, "edware": 9, "euston": 2},
            "euston": {"camden town": 2, "warren street": 1, "kings cross": 1},
            "warren street": {"euston": 1, "tottenham court road": 2, "oxford circus": 1},
            "tottenham court road": {"warren street": 2, "leicester square": 1, "oxford circus": 1, "holbourn": 1},
            "charing cross": {"leicester square": 1, "embankment": 1, "piccadilly circus": 1},
            "embankment": {"charing cross": 1, "waterloo": 1, "westminster": 1, "bank": 5},
            "waterloo": {"embankment": 1, "elephant & castle": 2, "westminster": 1, "london bridge": 2},
            "bank": {"moortage": 1, "london bridge": 1, "waterloo": 1, "holbourn": 3, "liverpool street": 1,"embankment": 5, "tower hill": 1, "shadwell": 1},
            "london bridge": {"bank": 1, "elephant & castle": 2, "waterloo": 2, "canada water": 2},
            "elephant & castle": {"london bridge": 2, "stockwell": 3, "waterloo": 2},
            "stockwell": {"waterloo": 3, "elephant & castle": 3, "morden": 9},
            "morden": {"stockwell": 9},
            "walthamstow central": {"finsbury park": 4},
            "highbury & islington": {"finsbury park": 1, "kings cross": 1, "west hampstead": 7, "stratford": 6},
            "oxford circus": {"warren street": 1, "green park": 1, "baker street": 2, "piccadilly circus": 1,"bond street": 1, "tottenham court road": 1},
            "victoria": {"green park": 1, "stockwell": 3, "south kensington": 2, "westminster": 2},
            "brixton": {"stockwell": 1},
            "harrow & wealdstone": {"willesden junction": 7},
            "willesden junction": {"harrow & wealdstone": 7, "paddington": 6, "richmond": 5, "west hampstead": 4},
            "paddington": {"willesden junction": 6, "baker street": 3, "notting hill gate": 2, "edgware road": 1,"hammersmith": 8},
            "west ruislip": {"notting hill gate": 12},
            "ealing broadway": {"notting hill gate": 7},
            "notting hill gate": {"west ruislip": 12, "ealing broadway": 7, "bond street": 4, "earls court": 2,
            "gloucester road": 2, "paddington": 2},
            "bond street": {"notting hill gate": 4, "oxford circus": 1, "baker street": 1, "green park": 1},
            "holbourn": {"tottenham court road": 1, "bank": 3},
            "mile end": {"liverpool street": 2, "stratford": 1, "whitechapel": 2, "bow": 1},
            "stratford": {"mile end": 1, "epping": 10, "west ham": 1, "bow": 2, "highbury & islington": 6},
            "epping": {"stratford": 10},
            "richmond": {"hammersmith": 6, "willesden junction": 5},
            "wimbledon": {"earls court": 8},
            "olympia": {"earls court": 1},
            "edgware road": {"paddington": 1, "baker street": 1},
            "westminster": {"victoria": 2, "embankment": 1, "green park": 1, "waterloo": 1},
            "tower hill": {"bank": 1, "aldgate east": 1, "liverpool street": 1, "shadwell": 1},
            "aldgate east": {"tower hill": 1, "whitechapel": 1, "liverpool street": 1},
            "whitechapel": {"aldgate east": 1, "mile end": 2, "shoreditch": 1, "shadwell": 1},
            "west ham": {"bow": 2, "barking": 4, "canning town": 1, "stratford": 1},
            "barking": {"west ham": 4, "upminster": 8},
            "upminster": {"barking": 8},
            "bow": {"mile end": 1, "west ham": 2, "poplar": 1, "stratford": 2},
            "shoreditch": {"whitechapel": 1},
            "shadwell": {"whitechapel": 1, "canada water": 3, "bank": 1, "tower hill": 1, "poplar": 3,"canary warf": 4},
            "canada water": {"shadwell": 3, "new cross": 2, "new cross gate": 2, "london bridge": 2, "canary wharf": 1},
            "new cross": {"canada water": 2},
            "new cross gate": {"canada water": 2},
            "stanmore": {"wembley park": 4},
            "west hampstead": {"wembley park": 5, "finchley road": 1, "willesden junction": 4,"highbury & islington": 7},
            "canary wharf": {"canada water": 1, "canning town": 2, "poplar": 2, "shadwell": 4, "lewisham": 10},
            "canning town": {"canary wharf": 2, "west ham": 1, "poplar": 3, "custom house": 2},
            "poplar": {"shadwell": 3, "canary wharf": 2, "bow": 1, "canning town": 3},
            "lewisham": {"canary wharf": 10},
            "custom house": {"canning town": 2, "beckton": 6, "north woolwich": 2},
            "beckton": {"custom house": 6},
            "north woolwich": {"custom house": 2},
        }

distancia, ruta = dijkstra(grafo, "Euston", "Moorgate")
rutafinal=""
for i in range(len(ruta)):
    rutafinal=rutafinal+str(ruta[i])+"->"
print("La distancia mínima requerida para el trayecto es de "+str(distancia)+", para la cual hay que seguir la siguiente ruta: "+rutafinal[:-2])