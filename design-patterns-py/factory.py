# The Factory Concept

from abc import ABCMeta, abstractmethod

class IProduct (metaclass=ABCMeta):
    "A hypothetical class interface (Product)"

    @staticmethod
    @abstractmethod

    def create_object():
        "An abstratic interface method"

class ConcreteProductA(IProduct):
    "A concrete class that implements the IProduct interface"

    def __init__(self):
        self.name = 'ConcreteProductA'
    
    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    "A concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = 'ConcreteProductB'

    def create_object(self):
        return self

class ConcreteProductC(IProduct):
    "A concrete class that implements the IProduct interface"

    def __init__(self):
        self.name = 'ConcreteProductC'

    def create_object(self):
        return self

class Creator:
    "The Factor Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"

        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None

PRODUCT = Creator().create_object('b')
print(PRODUCT.name)