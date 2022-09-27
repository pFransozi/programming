from abc import ABCMeta, abstractmethod

class IChair(metaclass=ABCMeta):
    "The chair interface (product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface mehtod"