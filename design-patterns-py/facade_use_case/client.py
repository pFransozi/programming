import time
from decimal import Decimal
from game_api import GameAPPI


USER = {"user_name":"sean"}
USER_ID = GameAPPI.register_user(USER)

time.sleep(1)

GameAPPI.submit_entry(USER_ID, Decimal('5'))

time.sleep(1)

print()
print("----------Game State Snapshot -----------")
print(GameAPPI.game_state())

time.sleep(1)


HISTORY = GameAPPI.get_history()

print()
print("Reports history")

for row in HISTORY:
    print(f"{row} : {HISTORY[row][0]} : {HISTORY[row][1]}")

print()
print("Gamestate snapshot")
print(GameAPPI.game_state())