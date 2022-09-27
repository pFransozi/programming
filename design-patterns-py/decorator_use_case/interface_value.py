from abc import ABCMeta, abstractmethod

class IValue(metaclass=ABCMeta):
    "methods the component must implement"

    @staticmethod
    @abstractmethod
    def __str__():
        "overide the object to return the value attribute by default"