import random

def crealaberinto():
    # Generar un número aleatorio de intersecciones (entre 5 y 15)
    num_intersecciones = random.randint(5, 15)
    
    # Crear la entrada y las dos salidas (intersecciones 0, num_intersecciones+1 y num_intersecciones+2)
    entrada = {"id": 0, "conexiones": [{"id": 1, "longitud": random.randint(1, 10), "direccion": "i"}]}
    salida_1 = {"id": num_intersecciones+1, "conexiones": []}
    salida_2 = {"id": num_intersecciones+2, "conexiones": []}

    # Crear las intersecciones y conectarlas entre sí
    intersecciones = [entrada, salida_1, salida_2]

    for i in range(1, num_intersecciones+1):
        # Elegir aleatoriamente las intersecciones a las que se va a conectar
        conexiones = []
        while len(conexiones) < 2:
            conexion = random.randint(1, num_intersecciones)
            if conexion != i and not any([c["id"] == conexion for c in conexiones]):
                conexiones.append({"id": conexion, "longitud": random.randint(1, 10), "direccion": random.choice(["i", "iv"])})
        interseccion = {"id": i, "conexiones": conexiones}
        intersecciones.append(interseccion)

    # Asegurarse de que todas las intersecciones están conectadas
    conectadas = [0]
    por_conectar = list(range(1, num_intersecciones+1))
    while por_conectar:
        interseccion_1 = random.choice(conectadas)
        interseccion_2 = random.choice(por_conectar)
        longitud = random.randint(1, 10)
        direccion = random.choice(["i", "iv"])
        intersecciones[interseccion_1]["conexiones"].append({"id": interseccion_2, "longitud": longitud, "direccion": direccion})
        intersecciones[interseccion_2]["conexiones"].append({"id": interseccion_1, "longitud": longitud, "direccion": direccion})
        conectadas.append(interseccion_2)
        por_conectar.remove(interseccion_2)

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

    # Mientras no lleguemos a una salida, seguimos avanzando aleatoriamente
    while actual["id"] not in [intersecciones[1]["id"], intersecciones[2]["id"]]:
        # Elegimos una conexión aleatoria
        posibles_destinos = [(conexion["id"], conexion["direccion"]) for conexion in actual["conexiones"] if (conexion["direccion"] == "iv" or conexion["id"] > actual["id"])]
        if len(posibles_destinos) == 0:
            print("¡Estamos atrapados!")
            break
        destino, direccion = random.choice(posibles_destinos)
        # Actualizamos el camino
        if direccion == 'i':
            if destino > actual["id"]:
                camino.append(destino)
        else:
            camino.pop()
            camino.append(destino)
        # Avanzamos a la siguiente intersección
        actual = next((item for item in intersecciones if item["id"] == destino), None)

    # Hemos llegado a una salida, imprimimos el camino
    print("Hemos llegado a la salida pasando por las intersecciones:")
    print(" -> ".join(str(i) for i in camino))

laberinto=crealaberinto()
recorrelaberinto(laberinto)
