from board import Board
from player import Player

class Game:
    def __init__(self, turn=0):
        self.turn = turn
        self.player1 = None
        self.player2 = None
        self.board = Board()

    # set player1
    def set_player1(self, player: Player):
        self.player1 = player

    # set player2
    def set_player2(self, player: Player):
        self.player2 = player

    def play(self):
        if not self.player1 or not self.player2:
            print("Can not start game without two players")
            return
        # make current player is player1 if it's turn = 0 or player2
        current_player = self.player1 if self.turn == 0 else self.player2
        # loop until win or draw and switch turn each loop
        while True:
            self.board.display()
            # make move by current player
            current_player.make_move(self.board)
            # get winner status either 'X' or 'O' or None
            winner = self.board.check_winner()

            # if it's not None means a current player win
            if winner:
                self.board.display()
                print(f"{current_player.name} ({current_player.symbol}) wins")
                break

            # check there is no slot free to declare a Draw and end game
            if self.board.is_full():
                self.board.display()
                print("Draw")
                break

            # switch turns and current player
            self.switch_turns()
            current_player = self.player1 if self.turn == 0 else self.player2

    def switch_turns(self):
        # negate turns if 0 wil be 1 - 0 = 0 , and if 1 will be 1-1 = 0
        self.turn = 1 - self.turn