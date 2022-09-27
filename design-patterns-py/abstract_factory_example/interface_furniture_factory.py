from abc import ABCMeta, abstractmethod

class IFurnitureFactory(metaclass=ABCMeta):
    "Abstract Furniture Factory Interface"

    @staticmethod
    @abstractmethod
    def get_furniture(Furniture):
        "The static abstratic factory interface method."