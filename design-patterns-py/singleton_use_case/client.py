from game1 import Game1
from game2 import Game2
from game3 import Game3

# All games share and manage the same leaderboard because
# it is a singleton

GAME1 = Game1()
GAME1.add_winner(2, "Cosmos")

GAME2 = Game2()
GAME2.add_winner(3, "Sean")

GAME3 = Game3()
GAME3.add_winner(1, "Emmy")

GAME1.leaderboard.print()
GAME2.leaderboard.print()
GAME3.leaderboard.print()

print("=============================")
print(id(GAME1.leaderboard))
print(id(GAME2.leaderboard))
print(id(GAME3.leaderboard))