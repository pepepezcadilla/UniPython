import socket
import threading
import sqlite3
import random
import json
import time

# Inicialización del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Cambia a la dirección IP del servidor
port = 12345
server.bind((host, port))
server.listen()

print("Servidor esperando conexiones...")

# Base de datos SQLite para el ranking
conn = sqlite3.connect('ranking.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  wins INTEGER,
                  draws INTEGER,
                  losses INTEGER
                  )''')
conn.commit()

# Lista de clientes conectados
clients = {}
player_names = {}

# Variable para contar el número de jugadores que se han unido
player_count = 0

# Función para manejar a un cliente
def handle_client(client):
    global player_count, current_player, game_mode, name
    # Recibir el mensaje del cliente
    message = client.recv(1024).decode()

    # Deserializar la cadena JSON para obtener los datos
    data_received = json.loads(message)

    # Obtener el nombre del jugador y el modo de juego
    name = data_received["name"]
    game_mode = data_received["game_mode"]
    player_names[client] = name
    clients[name] = client

    print(f"{name} se ha conectado desde {client.getpeername()}")

    current_player = ''
    player_count += 1

    if game_mode == "m":
        # Si el modo de juego es "M", crea la máquina como un cliente adicional
        machine_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        machine_name = "maquina"
        clients[machine_name] = machine_client
        player_names[machine_client] = machine_name
        machine_thread = threading.Thread(target=start_game, args=(machine_client, game_mode))
        machine_thread.start()
    elif player_count == 1:
        client.send("Esperando a otro jugador...".encode())
    elif player_count == 2:
        client.send("El juego ha comenzado. Empieza el jugador 1.".encode())
        start_game(client, game_mode)
    else:
        client.send("Lo siento, ya hay dos jugadores en juego.".encode())
        remove_client(client)
        return



# Función para que la máquina realice un movimiento aleatorio
def machine_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r * 3 + c] == ""]
    return random.choice(empty_cells)
# Funcion para cambiar de jugador
def changePlayer(current_player, player1, player2):
    if current_player == player1:
        if game_mode == 'm':
            current_player = 'maquina'
        else: 
            current_player = player2
    else: 
        current_player = player1
    broadcast('Cambio', 'Anonymous')
# Función para transmitir mensajes a todos los clientes
def broadcast(message, sender_client):
    # Crear una copia del diccionario
    clients_copy = clients.copy()

    for name, client in clients_copy.items():
        if name != sender_client and name != "maquina":
            client.send(message.encode())
            time.sleep(0.5)

# Función para eliminar a un cliente de la lista
def remove_client(client):
    if client in clients.values():
        name_to_remove = None
        for name, c in clients.items():
            if c == client:
                name_to_remove = name
                break
        if name_to_remove:
            del clients[name_to_remove]
            del player_names[client]

# Función para actualizar el ranking
def update_ranking(player_name, result):
    cursor.execute("SELECT * FROM players WHERE name=?", (player_name,))
    player = cursor.fetchone()

    if player is None:
        cursor.execute("INSERT INTO players (name, wins, draws, losses) VALUES (?, ?, ?, ?)",
                       (player_name, 0, 0, 0))
        conn.commit()

    if result == player_name:
        cursor.execute("UPDATE players SET wins=wins+1 WHERE name=?", (player_name,))
    elif result == "Draw":
        cursor.execute("UPDATE players SET draws=draws+1 WHERE name=?", (player_name,))
    else:
        cursor.execute("UPDATE players SET losses=losses+1 WHERE name=?", (player_name,))

    conn.commit()

# Función para iniciar el juego
def start_game(client, game_mode):
    broadcast('GameStart', 'Anonymous')
    players = list(clients.keys())
    global player1, player2
    player1 = players[1]
    player2 = players[2]

    # Asigna el símbolo correspondiente a cada jugador
    symbol1 = "X"
    symbol2 = "O"
    client1 = clients[player1]
    client2 = clients[player2]
    print(client1, client2)
    client1.send(f"Symbol:{symbol1}".encode())
    if(game_mode != 'm'):
        client2.send(f"Symbol:{symbol2}".encode())
    time.sleep(0.5)
    # Tablero de juego
    board = [""] * 9
    current_player = player1
    current_client = client1
    print(players)
    while True:
        if current_player == "maquina" and game_mode == "m":
            row, col = machine_move(board)
        else:
            current_client.send(f"Your Turn:".encode())
            move = current_client.recv(1024).decode()
            print(f"{name} ha realizado un movimiento: {move[5:]}")
            row, col = map(int, move[5:])

        index = row * 3 + col

        #if board[index] == "":
            #   board[index] = symbol1 if current_player == player1 else symbol2
            #  broadcast(f"Board:{''.join(board)}", current_client)
#
#               if check_winner(board, symbol1):
#                  update_ranking(player1, player1)
#                 broadcast(f"Result:{player1}", current_client)
#                return
    #           elif check_winner(board, symbol2):
    #              update_ranking(player2, player2)
    #             broadcast(f"Result:{player2}", current_client)
    #            return
        #       elif "" not in board:
        #          update_ranking(player1, "Draw")
        #         update_ranking(player2, "Draw")
        #        broadcast("Result:Draw", current_client)
            #       return

        # Muestra el tablero después del movimiento
        #broadcast(f"Board:{''.join(board)}", current_client)

        # Cambio de jugador
        print(current_player)
        current_player = changePlayer(current_player, player1, player2)

        if current_player == "maquina" and game_mode == "M":
            break



# Función para comprobar si hay un ganador
def check_winner(board, symbol):
    for i in range(3):
        if all(board[i * 3 + j] == symbol for j in range(3)) or all(board[j * 3 + i] == symbol for j in range(3)):
            return True
    return board[0] == board[4] == board[8] == symbol or board[2] == board[4] == board[6] == symbol

# Ciclo principal para aceptar conexiones de clientes
while True:
    client, address = server.accept()
    print(f"Conexión establecida desde {address[0]}:{address[1]}")
    clients[player_names.get(client, 'Anonymous')] = client
    # Inicia un hilo para manejar al cliente
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
