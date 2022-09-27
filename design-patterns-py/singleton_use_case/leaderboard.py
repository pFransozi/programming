"A leaderboard singleton class"

class Leaderboard():
    "The leaderboard as a singleton"

    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        "a class level method"
        print("---------------Leaderboard---------------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value}\t|")
        
        print()

    @classmethod
    def add_winner(cls, position, name):
        "A class level method"
        cls._table[position] = name