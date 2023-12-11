import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter#here letter is the input we take either x or o

    def get_move(slef, game):
        pass

class RandomComputerPlayer():
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid sport for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print("Invalid square. Try again.")
        return val