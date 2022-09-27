"Prototype Concept Sample Code"
from abc import ABCMeta, abstractmethod

class IPrototype(metaclass=ABCMeta):
    "interface with clone method"

    @staticmethod
    @abstractmethod
    def clone(mode):
        '''
        the clone, deep or shallow. It is up to you how
        you want implement the details in your concrete class
        '''
