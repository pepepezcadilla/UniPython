import tkinter as tk
import numpy as np

class FourInARowApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("4 en raya")
        self.board = np.zeros((6, 7))
        self.turn = 1
        self.canvas = tk.Canvas(self.window, width=1000, height=1000, bg="blue")
        self.canvas.pack()
        self.draw_board()
        self.reset_button = tk.Button(self.window, text="Reiniciar", command=self.reset_board, state=tk.DISABLED)
        self.reset_button.pack()
        self.canvas.bind("<Button-1>", self.drop_piece)
        self.window.mainloop()

    def draw_board(self):
        for row in range(6):
            for col in range(7):
                x1 = col * 100 + 50
                y1 = row * 100 + 50
                x2 = x1 + 100
                y2 = y1 + 100
                self.canvas.create_oval(x1, y1, x2, y2, fill="white")

    def drop_piece(self, event):
        col = event.x // 100
        row = 0
        while row < 6 and self.board[row][col] == 0:
            row += 1
        if row > 0:
            row -= 1
            player = self.turn % 2 + 1
            self.board[row][col] = player
            x = col * 100 + 50
            y = row * 100 + 50
            if player == 1:
                self.canvas.create_oval(x, y, x + 100, y + 100, fill="red")
            else:
                self.canvas.create_oval(x, y, x + 100, y + 100, fill="yellow")
            self.turn += 1
            if self.check_win(row, col, player):
                self.canvas.unbind("<Button-1>")
                self.reset_button.configure(state=tk.NORMAL)
                tk.messagebox.showinfo("Victoria", f"¡El jugador {player} ha ganado!")
            elif self.check_tie():
                self.canvas.unbind("<Button-1>")
                self.reset_button.configure(state=tk.NORMAL)
                tk.messagebox.showinfo("Empate", "¡El juego ha terminado en empate!")

    def check_win(self, row, col, player):
        for i in range(-3, 1):
            if col + i < 0 or col + i > 6:
                continue
            if self.board[row][col+i] == player and self.board[row][col+i+1] == player and self.board[row][col+i+2] == player and self.board[row][col+i+3] == player:
                return True
        for i in range(-3, 1):
            if row + i < 0 or row + i > 5:
                continue
            if col + i < 0 or col + i > 6:
                continue
            if self.board[row+i][col+i] == player and self.board[row+i+1][col+i+1] == player and self.board[row+i+2][col+i+2] == player and self.board[row+i+3][col+i+3] == player:
                return True
        for i in range(-3, 1):
            if row + i < 0 or row + i > 5:
                continue
            if col - i < 0 or col - i > 6:
                continue
            if self.board[row+i][col-i] == player and self.board[row+i+1][col-i-1] == player and self.board[row+i+2][col-i-2] == player and self.board[row+i+3][col-i-3] == player:
                return True
        for i in range(-3, 1):
            if row + i < 0 or row + i > 5:
                continue
            if self.board[row+i][col] == player and self.board[row+i+1][col] == player and self.board[row+i+2][col] == player and self.board[row+i+3][col] == player:
                return True
        return False

    def check_tie(self):
        return np.all(self.board != 0)

    def reset_board(self):
        self.board = np.zeros((6, 7))
        self.turn = 1
        self.canvas.delete("all")
        self.draw_board()
        self.canvas.bind("<Button-1>", self.drop_piece)
        self.reset_button.configure(state=tk.DISABLED)


app = FourInARowApp()