#Wajed Basbous
#Rudy Abou Assaly
#Ali Mansour

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 16), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if not self.buttons[row][col]['text']:
            self.buttons[row][col]['text'] = self.current_player
            if self.check_win(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"{self.current_player} Wins!")
                self.reset_game()
            elif self.tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.computer_turn()

    def check_win(self, player):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] == player:
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] == player:
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] == player:
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] == player:
            return True

        return False

    def tie(self):
        for i in range(3):
            for j in range(3):
                if not self.buttons[i][j]['text']:
                    return False
        return True

    def computer_turn(self):
        if not self.tie():
            move = self.minimax()
            self.buttons[move.x][move.y]['text'] = self.current_player
            if self.check_win(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"{self.current_player} Wins!")
                self.reset_game()
            elif self.tie():
                messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
                self.reset_game()
            else:
                self.current_player = "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
        self.current_player = "X"

    def minimax(self):
        score = float('-inf')
        move = self.Move()

        for i in range(3):
            for j in range(3):
                if not self.buttons[i][j]['text']:
                    self.buttons[i][j]['text'] = self.current_player
                    temp = self.min_search()

                    if temp > score:
                        score = temp
                        move.x = i
                        move.y = j

                    self.buttons[i][j]['text'] = ""

        return move

    def max_search(self):
        if self.check_win("X"):
            return -10
        elif self.check_win("O"):
            return 10
        elif self.tie():
            return 0

        score = float('-inf')

        for i in range(3):
            for j in range(3):
                if not self.buttons[i][j]['text']:
                    self.buttons[i][j]['text'] = "O"
                    score = max(score, self.min_search())
                    self.buttons[i][j]['text'] = ""

        return score

    def min_search(self):
        if self.check_win("X"):
            return -10
        elif self.check_win("O"):
            return 10
        elif self.tie():
            return 0

        score = float('inf')

        for i in range(3):
            for j in range(3):
                if not self.buttons[i][j]['text']:
                    self.buttons[i][j]['text'] = "X"
                    score = min(score, self.max_search())
                    self.buttons[i][j]['text'] = ""

        return score

    class Move:
        def __init__(self):
            self.x = 0
            self.y = 0

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
