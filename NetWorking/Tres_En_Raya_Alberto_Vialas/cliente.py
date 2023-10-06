import socket
import tkinter as tk
from tkinter import messagebox
import threading
import json

# Función para solicitar el modo de juego al usuario
def choose_game_mode():
    while True:
        mode = input("¿Deseas jugar contra otro jugador (J) o contra la máquina (M)? ").strip().upper()
        if mode == "J":
            return "J"
        elif mode == "M":
            return "M"
        else:
            print("Por favor, ingresa 'J' para jugar contra otro jugador o 'M' para jugar contra la máquina.")

# Configuración del cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Cambia a la dirección IP del servidor
port = 12345

# Solicitar el modo de juego por consola
game_mode = choose_game_mode()

# Solicitar el nombre de usuario por consola
player_name = input("Ingresa tu nombre de jugador (que quedará registrado en el ranking): ")   

# Crear un diccionario con los datos a enviar
data_to_send = {
    "name": player_name,
    "game_mode": game_mode
}

# Serializar el diccionario a una cadena JSON
message = json.dumps(data_to_send)

# Conectar al servidor
client.connect((host, port))

# Enviar la cadena JSON al servidor
client.send(message.encode())

# Ventana de juego
root = tk.Tk()
root.title("Tres en Raya")
print("aaa")
# Variables globales
symbol = ""
current_player = ""
buttons = []
game_over = False

# Variable para indicar si el juego ha comenzado
game_started = False

# Función para enviar un movimiento al servidor
def send_move(row, col):
    if current_player == player_name and not game_over:
        move = f"Move:{row}{col}"
        client.send(move.encode())

# Función para manejar los movimientos recibidos del servidor
def handle_move(move):
    if not game_over:
        row, col = int(move[5]), int(move[6])
        button = buttons[row][col]
        if button["text"] == "":
            button["text"] = symbol
            check_game_over()

# Función para comprobar si el juego ha terminado
def check_game_over():
    global game_over
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return

    game_over = True
    client.send("Result:Draw".encode())
    show_result("Draw")

# Función para mostrar un mensaje de ganador o empate
def show_result(result):
    if result == "Draw":
        messagebox.showinfo("¡Empate!", "El juego ha terminado en empate.")
    else:
        messagebox.showinfo("¡Ganador!", f"El ganador es el jugador {result}.")
    root.quit()

# Función para manejar el flujo del juego
def game_flow():
    global current_player, game_started
    while True:
        try:
            message = client.recv(1024).decode()
            if message.startswith("Symbol:"):
                global symbol
                symbol = message.split(":")[1]
                if symbol == "X":
                    current_player = player_name
                else:
                    current_player = "Jugador 2"
            elif message.startswith("Board:"):
                board = message.split(":")[1]
                for row in range(3):
                    for col in range(3):
                        buttons[row][col]["text"] = board[row * 3 + col]
            elif message.startswith("Result:"):
                result = message.split(":")[1]
                show_result(result)
            elif message.startswith("Your Turn:"):
                current_player = player_name
        except:
            break

# Esperar hasta que el juego haya comenzado
if not game_started:
    game_started = client.recv(1024).decode()

# Ventana de juego principal
game_window = tk.Toplevel(root)
game_window.title("Tres en Raya")

for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(game_window, text="", font=("Helvetica", 20), width=5, height=2,
                           command=lambda row=row, col=col: send_move(row, col))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Iniciar hilo para el flujo del juego
game_thread = threading.Thread(target=game_flow)
game_thread.start()

root.mainloop()
