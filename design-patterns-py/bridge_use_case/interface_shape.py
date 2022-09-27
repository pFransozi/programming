from abc import ABCMeta, abstractmethod

class IShape(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def draw():
        "The method that will be handled at the shapes' implement"