import tkinter as tk
from tkinter import messagebox



def create_buttons():
    buttons = []
    for i in range(3):
        row_buttons = []
        for j in range(3):
            btn = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                            command=lambda row=i, col=j: on_click(row, col))
            btn.grid(row=i, column=j, padx=5, pady=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)
    return buttons


def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not winner:
        buttons[row][col]["text"] = current_player
        check_winner(row, col)
        toggle_player()



def check_winner(row, col):
    global winner
    if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
        winner = True
    elif buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
        winner = True
    elif buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        winner = True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        winner = True

    if winner:
        messagebox.showinfo("Tic Tac Toe", f"¡El jugador {current_player} ha ganado!")
        reset_game()
    elif all(button["text"] for row in buttons for button in row):
        messagebox.showinfo("Tic Tac Toe", "¡Es un empate!")
        reset_game()


def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def create_buttons():
    buttons = []
    for i in range(3):
        row_buttons = []
        for j in range(3):
            btn = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                            command=lambda row=i, col=j: on_click(row, col), bg="lightblue", fg="black")
            btn.grid(row=i, column=j, padx=5, pady=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)
    return buttons

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not winner:
        buttons[row][col]["text"] = current_player
        buttons[row][col]["fg"] = "red" if current_player == "X" else "blue"
        check_winner(row, col)
        toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"



def reset_game():
    global winner
    winner = False
    for row in buttons:
        for button in row:
            button["text"] = "" 
    play_again_button = tk.Button(root, text="Jugar de Nuevo", font=('normal', 20),
                                  command=lambda: [reset_game(), play_again_button.destroy()])
    play_again_button.grid(row=3, column=0, columnspan=3)


root = tk.Tk()
root.title("Tic Tac Toe")

buttons = create_buttons()
current_player = "X"
winner = False



root.mainloop()