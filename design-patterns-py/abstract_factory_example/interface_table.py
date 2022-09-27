from abc import ABCMeta, abstractmethod

class ITable(metaclass=ABCMeta):
    "The table interface (product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method."