import random
from abc import ABC, abstractmethod
from board import Board


class Player(ABC):
    def __init__(self, name="Computer", symbol="X"):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board: Board):
        pass

class HumanPlayer(Player):
    def __init__(self, name="Human", symbol="X"):
        super().__init__(name, symbol)

    def make_move(self, board: Board):
        while True:
            try:
                # get position as comma separated integars from 0 to 2
                pos = input(f"{self.name} ({self.symbol}), enter your move as row,col (0-2): ")
                row, col = map(int, pos.strip().split(","))
                if 0 <= row < 3 and 0 <= col < 3:
                    if board.update((row, col), self.symbol):
                        return
                    else:
                        print("Cell already taken. Try again.")
                else:
                    print("Invalid position. Try again.")
            except Exception:
                print("Invalid input. Try again.")

class ComputerPlayer(Player):
    def __init__(self, name="Computer", symbol="O"):
        super().__init__(name, symbol)

    def make_move(self, board: Board):
        # get empty slot and choose a random one from
        empty = [(r, c) for r in range(3) for c in range(3) if board.grid[r][c] == "_"]
        if empty:
            move = random.choice(empty)
            board.update(move, self.symbol)
            print(f"{self.name} ({self.symbol}) played at {move[0]},{move[1]}")