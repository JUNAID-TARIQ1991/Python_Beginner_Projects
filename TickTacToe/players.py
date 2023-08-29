import math
import random


class Players:
    def __init__(self, letter):
        # letter x or p
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Players):
    def __init__(self, letter):
        self.letter = letter
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Players):
    def __init__(self, letter):
        self.letter = letter
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input moves (0-9):')
