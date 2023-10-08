import socket
import tkinter as tk
from tkinter import messagebox
import threading
import json
import time

# Función para solicitar el modo de juego al usuario
def choose_game_mode():
    while True:
        mode = input("¿Deseas jugar contra otro jugador (J) o contra la máquina (M)? ").strip().lower()
        if mode == "j":
            return "j"
        elif mode == "m":
            return "m"
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

# Variables globales
symbol = ""
current_player = ""
buttons = []
game_over = False

# Variable para indicar si el juego ha comenzado
game_started = False

# Función para manejar el clic del usuario en un botón del tablero
def handle_button_click(row, col):
    if current_player == player_name and not game_over:
        if buttons[row][col]["text"] == "":
            buttons[row][col]["text"] = str(symbol)
            # Llama a send_move para enviar el movimiento al servidor
            send_move(row, col)
        else:
            print("La casilla ya está ocupada. Elige otra.")
    else:
        print("No es tu turno. Espera a tu turno para realizar un movimiento.")

# Función para enviar un movimiento al servidor
def send_move(row, col):
    if current_player == player_name and not game_over:
        move = f"Move:{row}{col}"
        print(f"Enviado movimiento: {move}")
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
    global current_player, game_started, game_over, clicked_button, symbol
    clicked_button = tk.StringVar()
    while not game_over:
        print('again')
        try:
            message = client.recv(1024).decode()
            print(message)
            if message.startswith("Symbol:"):
                symbol = message.split(":")[1]
                if symbol == "X":
                    current_player = player_name
                else:
                    current_player = "Jugador 2"
            
            elif message.startswith("Your Turn:"):
                current_player = player_name
                print("Es tu turno. Selecciona una casilla (fila y columna):")
            
            elif message.startswith("Board:"):
                board = message.split(":")[1]
                # Actualiza el tablero con la información recibida
                handle_move(board)
            
            elif message.startswith("Result:"):
                result = message.split(":")[1]
                show_result(result)
                game_over = True
            
            elif message.startswith('Cambio'):
                current_player = "Jugador 2"
        
        except Exception as e:
            print("Error:", e)
            break

# Esperar hasta que el juego haya comenzado
while True:
    game_status = client.recv(1024).decode()
    print(game_status)
    if game_status == 'GameStart':
        print("El juego ha comenzado.")
        break

# Ventana de juego principal
game_window = tk.Toplevel(root)
game_window.title("Tres en Raya")

for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(game_window, text="", font=("Helvetica", 20), width=5, height=2,
                           command=lambda row=row, col=col: handle_button_click(row, col))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Iniciar hilo para el flujo del juego
game_thread = threading.Thread(target=game_flow)
game_thread.start()

root.mainloop()
