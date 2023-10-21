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
conn = sqlite3.connect('./ranking.db')
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
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                empty_cells.append([i, j])
    a = random.choice(empty_cells)
    return a

def update_board(board, row, col, symbol):
    if board[row][col] == "":
        board[row][col] = symbol
    board_json = json.dumps(board)
    broadcast("Board:" + board_json, "Anonimous")
    return board

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
    return current_player

def check_winner(board, symbol):
    # Comprobar filas y columnas
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True

    # Comprobar diagonales
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

# Función para transmitir mensajes a todos los clientes
def broadcast(message, sender_client):
    # Crear una copia del diccionario
    clients_copy = clients.copy()

    for name, client in clients_copy.items():
        if name != sender_client and name != "maquina":
            client.send(message.encode())
            time.sleep(0.2)

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
def update_ranking(player_name):
    # Conexión a la base de datos (la creará si no existe)
    conn = sqlite3.connect('ranking.db')
    cursor = conn.cursor()

    # Comprueba si la tabla "players" existe, y si no, la crea
    cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  wins INTEGER
                  )''')
    conn.commit()

    # Verifica si el jugador ya está en la tabla
    cursor.execute("SELECT * FROM players WHERE name=?", (player_name,))
    player = cursor.fetchone()

    if player is None:
        # Si el jugador no existe, inserta un nuevo registro
        cursor.execute("INSERT INTO players (name, wins) VALUES (?, ?)", (player_name, 1))
    else:
        # Si el jugador existe, actualiza el número de victorias
        cursor.execute("UPDATE players SET wins=wins+1 WHERE name=?", (player_name,))

    conn.commit()

    # Ordena la tabla por número de victorias (más alta primero)
    cursor.execute("SELECT * FROM players ORDER BY wins DESC")
    ranked_players = cursor.fetchall()
    for idx, ranked_player in enumerate(ranked_players, start=1):
        print(f"{idx}. {ranked_player[1]} - Victorias: {ranked_player[2]}")

    # Cierra la conexión a la base de datos
    conn.close()

def disconnect_client(players):
    for player in players: 
        if player in clients:
            if player != "Anonymous":
                client = clients[player]
                client.close()  # Cierra el socket del cliente
                del clients[player]  # Elimina al cliente de la lista de clientes
                del player_names[client]  # Elimina el nombre del cliente
                print(f"{player} se ha desconectado.")

# Función para iniciar el juego
def start_game(client, game_mode):
    broadcast("GameStart", "Anonymous")
    players = list(clients.keys())
    global player1, player2
    player1 = players[1]
    player2 = players[2]
    gameNotOver = True
    # Asigna el símbolo correspondiente a cada jugador
    symbol1 = "X"
    symbol2 = "O"
    client1 = clients[player1]
    client2 = clients[player2]
    client1.send(f"Symbol:{symbol1}".encode())
    if(game_mode != 'm'):
        client2.send(f"Symbol:{symbol2}".encode())
    time.sleep(0.2)
    # Tablero de juego
    board = [["", "", ""],["", "", ""],["", "", ""]]
    current_player = player1
    current_client = client1
    while gameNotOver:
        if current_player == "maquina" and game_mode == "m":
            row, col = machine_move(board)
        else:
            current_client.send(f"Your Turn:".encode())
            move = current_client.recv(1024).decode()
            print(f"{name} ha realizado un movimiento: {move[5:]}")
            row, col = map(int, move[5:])

        if current_player == player1:
            board = update_board(board, row, col, "X")
        else:
            board = update_board(board, row, col, "O")

        if(check_winner(board, "X")):
            update_ranking(current_player)
            broadcast("Result: X GANA", "Anonymous")
            disconnect_client(players)
            gameNotOver = False
        elif(check_winner(board, "O")):
            update_ranking(current_player)
            broadcast("Result: O GANA", "Anonymous")
            disconnect_client(players)
            gameNotOver = False
            
        else:
            current_player = changePlayer(current_player, player1, player2)

        if current_player == "maquina" and game_mode == "M":
            break
        
# Función principal
def main():
    # Inicialización del servidor y otras configuraciones aquí...
    while True:
        client, address = server.accept()
        print(f"Conexión establecida desde {address[0]}:{address[1]}")
        clients[player_names.get(client, 'Anonymous')] = client
        # Inicia un hilo para manejar al cliente
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()
