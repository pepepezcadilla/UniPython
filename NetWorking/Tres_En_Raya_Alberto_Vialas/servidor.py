import socket
import threading
import sqlite3
import random
import json

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
    
    # Recibir el mensaje del cliente
    message = client.recv(1024).decode()

    # Deserializar la cadena JSON para obtener los datos
    data_received = json.loads(message)

    # Obtener el nombre del jugador y el modo de juego
    name = data_received["name"]
    game_mode = data_received["game_mode"]
    print(name)
    print(game_mode)
    player_names[client] = name
    clients[name] = client

    print(f"{name} se ha conectado desde {client.getpeername()}")

    global player_count
    player_count += 1

    if game_mode == "M":
        # Si el modo de juego es "M", crea la máquina como un cliente adicional
        machine_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #machine_client.connect((host, port))
        machine_name = "Máquina"
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

    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                if message.startswith("Move:"):
                    print(f"{name} ha realizado un movimiento: {message[5:]}")
                    broadcast(message, client)
        except:
            remove_client(client)
            break

    remove_client(client)

# Función para que la máquina realice un movimiento aleatorio
def machine_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r * 3 + c] == ""]
    return random.choice(empty_cells)

# Función para transmitir mensajes a todos los clientes
def broadcast(message, sender_client):
    for name, client in clients.items():
        if client != sender_client:
            try:
                client.send(message.encode())
            except:
                remove_client(client)

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
    broadcast(True, 'Anonymous')
    players = list(clients.keys())
    player1 = players[0]
    player2 = players[1]

    # Envía el símbolo correspondiente a cada jugador
    symbol1 = "X"
    symbol2 = "O"
    client1 = clients[player1]
    client2 = clients[player2]
    print(clients)
    client1.send(f"Symbol:{symbol1}".encode())
    client2.send(f"Symbol:{symbol2}".encode())

    # Tablero de juego
    board = [""] * 9

    while True:
        current_player = player1
        current_client = client1

        while True:
            if current_player == "Máquina" and game_mode == "M":
                row, col = machine_move(board)
            else:
                current_client.send(f"Your Turn:".encode())
                move = current_client.recv(1024).decode()
                row, col = map(int, move[5:])

            index = row * 3 + col

            if board[index] == "":
                board[index] = symbol1 if current_player == player1 else symbol2
                broadcast(f"Board:{''.join(board)}", current_client)

                if check_winner(board, symbol1):
                    update_ranking(player1, player1)
                    broadcast(f"Result:{player1}", current_client)
                    return
                elif check_winner(board, symbol2):
                    update_ranking(player2, player2)
                    broadcast(f"Result:{player2}", current_client)
                    return
                elif "" not in board:
                    update_ranking(player1, "Draw")
                    update_ranking(player2, "Draw")
                    broadcast("Result:Draw", current_client)
                    return

            if current_player == "Máquina" and game_mode == "M":
                break

            current_player, current_client = player2, client2

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
    client.send("Nombre de jugador: ".encode())
    print(client)
    # Inicia un hilo para manejar al cliente
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
