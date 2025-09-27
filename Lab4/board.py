class Board:
    def __init__(self):
        self.grid = [["_" for _ in range(3)] for _ in range(3)]

    def display(self):
        # draw row by row with | as separator 
        for row in self.grid:
            print(" | ".join(row))
        print("------------------------------------------\n")

    def update(self, position, symbol):
        # unpack position tuple
        row, col = position
        # if empty then put symbol and return success
        if self.grid[row][col] == "_":
            self.grid[row][col] = symbol
            return True

        # incorrect position return false
        return False

    def check_winner(self):
        # check same symbol either 'X' or 'O' is occured in any row
        for row in self.grid:
            if row[0] == row[1] == row[2] != "_":
                return row[0]
            
        # check same symbol either 'X' or 'O' is occured in any col
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != "_":
                return self.grid[0][col]

        # check same symbol either 'X' or 'O' is occured in diagnoal \
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != "_":
            return self.grid[0][0]
        
        # check same symbol either 'X' or 'O' is occured in diagnoal /
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != "_":
            return self.grid[0][2]
        
        # else no winner yet
        return None

    def is_full(self):
        # check if no _ in any slot in grid
        for row in self.grid:
            if "_" in row:
                return False
        return True

    def __str__(self):
        return "\n".join([" | ".join(row) for row in self.grid])