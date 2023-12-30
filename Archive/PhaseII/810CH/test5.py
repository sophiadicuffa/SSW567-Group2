''' Test 5 - https://chat.openai.com/share/3eb83f31-1b88-45ce-b951-dcaf0c7c6693 - convo link '''
# Rated 6.82
import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Initialize game board, player, etc.

        self.create_widgets()

    def create_widgets(self):
        # Create buttons for the Tic Tac Toe grid
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=4, command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_click(self, i, j):
        # Handle button click event
        pass
        # Implement game logic here

    # Implement game logic functions (turns, win check, etc.)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()