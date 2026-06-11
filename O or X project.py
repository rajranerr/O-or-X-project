import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)
        
        # Game variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        # UI Setup
        self.status_label = tk.Label(self.root, text="Player X's turn", font=('Helvetica', 14, 'bold'), pady=10)
        self.status_label.pack()
        
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()
        
        # 3x3 Button grid creation
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.grid_frame, 
                    text="", 
                    font=('Helvetica', 20, 'bold'), 
                    width=6, 
                    height=3,
                    command=lambda r=row, c=col: self.handle_click(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col, padx=2, pady=2)
                
        # Reset button
        self.reset_btn = tk.Button(self.root, text="Restart Game", font=('Helvetica', 11), command=self.reset_game, pady=5)
        self.reset_btn.pack(pady=10)

    def handle_click(self, row, col):
        # Validate move: ensure square is empty
        if self.board[row][col] == "":
            # Update internal logical matrix
            self.board[row][col] = self.current_player
            # Update visual button interface
            self.buttons[row][col].config(text=self.current_player, state="disabled", disabledforeground="black")
            
            # Check for endgame conditions
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_board()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                # Switch active turn
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, r, c):
        # Check specific row
        if all(self.board[r][i] == self.current_player for i in range(3)):
            return True
        # Check specific column
        if all(self.board[i][c] == self.current_player for i in range(3)):
            return True
        # Check primary diagonal
        if r == c and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        # Check anti-diagonal
        if r + c == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_tie(self):
        return all(self.board[r][c] != "" for r in range(3) for c in range(3))

    def disable_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.status_label.config(text="Player X's turn")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()