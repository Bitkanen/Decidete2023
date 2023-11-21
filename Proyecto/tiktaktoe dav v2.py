import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Colores
        self.bg_color = '#d9d9d9'
        self.button_bg_color = '#add8e6'
        self.x_color = '#ff0000'
        self.o_color = '#0000ff'
        self.button_fg_color = '#333333'


        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text='', font=('normal', 30),
                                              width=5, height=2, command=lambda i=i, j=j: self.on_click(i, j),
                                              bg=self.button_bg_color, fg=self.button_fg_color)
                self.buttons[i][j].grid(row=i, column=j)


        self.reset_button = tk.Button(self.master, text='Reiniciar', font=('normal', 18), command=self.reset_game,
                                      bg=self.button_bg_color, fg=self.button_fg_color)
        self.reset_button.grid(row=3, columnspan=3)


        self.master.configure(bg=self.bg_color)


        self.master.resizable(False, False)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            color = self.x_color if self.current_player == 'X' else self.o_color
            self.buttons[row][col].config(text=self.current_player, fg=color)
            if self.check_winner(row, col):
                messagebox.showinfo("¡Felicidades!", f"Jugador {self.current_player} ha ganado.")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Empate", "El juego ha terminado en empate.")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        if all(self.board[row][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='', fg=self.button_fg_color)
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
