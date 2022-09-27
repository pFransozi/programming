from abc import ABCMeta, abstractmethod

class ICubeA(metaclass=ABCMeta):
    "an interface for an object"

    @staticmethod
    @abstractmethod
    def manufacture(width, height, depth):
        "manufactures a cube"