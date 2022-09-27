from abc import ABCMeta, abstractmethod

class IGame(metaclass=ABCMeta):
    "a game interface"

    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        "must implement add_winner"