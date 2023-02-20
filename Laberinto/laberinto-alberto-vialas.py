import random


def crealaberinto():
    # Generar un número aleatorio de intersecciones (entre 5 y 15)
    #num_intersecciones = random.randint(5, 15)
    num_intersecciones = 10

    # Crear la entrada y las dos salidas (intersecciones 0, num_intersecciones+1 y num_intersecciones+2)
    long_ent = random.randint(1, 10)
    entrada = {"id": 0, "conexiones": [{"id": 1, "longitud": long_ent, "direccion": "i"}]}
    salida_1 = {"id": num_intersecciones+1, "conexiones": []}
    salida_2 = {"id": num_intersecciones+2, "conexiones": []}
    primera = {"id": 1, "conexiones": [{"id": 0, "longitud": long_ent, "direccion": "i"}]}
    # Crear las intersecciones y conectarlas entre sí
    intersecciones = [entrada, salida_1, salida_2, primera]
    for i in range(2, num_intersecciones):
        interseccion = {"id": i, "conexiones": []}
        intersecciones.append(interseccion)

    for i in range(1, num_intersecciones+1):
        # Elegir aleatoriamente las intersecciones a las que se va a conectar
        diccionario_1 = intersecciones[i]
        segundo=random.randint(i+1, num_intersecciones+1)
        diccionario_2 = intersecciones[segundo]
        num_conexiones1 = len(diccionario_1["conexiones"])
        num_conexiones2 = len(diccionario_2["conexiones"])
        if(num_conexiones2<4 and num_conexiones1<4):
            longitud = random.randint(1, 10)
            direccion = random.choice(["i", "iv", "iv"])
            intersecciones[i]["conexiones"].append({"id": diccionario_2["id"], "longitud": longitud, "direccion": direccion})
            intersecciones[segundo]["conexiones"].append({"id": diccionario_1["id"], "longitud": longitud, "direccion": direccion})

    # Imprimir el laberinto 
    for interseccion in intersecciones:
        print("Intersección", interseccion["id"])
        print("Conexiones:")
        for conexion in interseccion["conexiones"]:
            print("- Conexión con intersección", conexion["id"], "de longitud", conexion["longitud"], "en dirección", conexion["direccion"])
        print()
    return intersecciones

def recorrelaberinto(intersecciones):
   # Empezamos en la entrada
    actual = intersecciones[0]
    camino = [actual["id"]]
    MAX_ITERACIONES = 1000
    iteraciones = 0
    longitud_final = 0
    final = False

    # Mientras no lleguemos a una salida, seguimos avanzando aleatoriamente
    while actual["id"] not in [intersecciones[1]["id"], intersecciones[2]["id"]] and iteraciones < MAX_ITERACIONES:
        print(actual["id"], intersecciones[1]["id"], intersecciones[2]["id"])
        print(len(intersecciones))
        if actual["id"] in [intersecciones[1]["id"], intersecciones[2]["id"]]:
            final = True
            break
        # Elegimos una conexión aleatoria
        posibles_destinos = [(conexion["id"], conexion["longitud"], conexion["direccion"]) for conexion in actual["conexiones"] if (conexion["direccion"] == "iv" or conexion["id"] > actual["id"])]
        if len(posibles_destinos) == 0:
            print("¡Estamos atrapados!")
            break
        destino, longitud, direccion = random.choice(posibles_destinos)
        # Actualizamos el camino y la lista de visitados
        if direccion == 'i':
            if destino > actual["id"]:
                camino.append(destino)
                longitud_final += longitud
                actual = next((item for item in intersecciones if item["id"] == destino), None) 
        else:
            camino.append(destino)
            longitud_final += longitud
            actual = next((item for item in intersecciones if item["id"] == destino), None) 
            

        iteraciones += 1

    # Hemos llegado a una salida, imprimimos todas las intersecciones visitadas
    if(final):
        print("Hemos llegado a la salida pasando por las intersecciones:")
        print(" -> ".join(str(i) for i in camino))
        print("Hemos tardado: ", longitud_final)
    else:
        print("Número de intentos demasiado alto. Hemos perdido.")

laberinto=crealaberinto()
recorrelaberinto(laberinto)
