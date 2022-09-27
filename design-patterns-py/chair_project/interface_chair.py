"The Chair Interface"
from abc import ABCMeta, abstractmethod

class IChair(metaclass=ABCMeta):
    "The Chair Interfaces (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"