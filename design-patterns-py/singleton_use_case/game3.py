"A game class that uses the leaderboard singleton"

from leaderboard import Leaderboard
from interface_game import IGame

class Game3(IGame):

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)