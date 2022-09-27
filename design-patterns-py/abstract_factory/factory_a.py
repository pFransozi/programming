from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    # A hypothetical class interface (Product)

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"

class ConcreteProductA(IProduct):

    def __init__(self):
        self.names = 'ConcreteProductA'
    
    def create_object(self):
        return self

class ConcreteProductB(IProduct):

    def __init__(self):
        self.name = 'ConcreteProductB'
    
    def create_object(self):
        return self

class ConcreteProductC(IProduct):

    def __init__(self):
        self.name = 'ConcreteProductC'
    
    def create_object():
        return self

class FactoryA:

    @staticmethod
    def create_object(some_property):

        try:
            if some_property == 'a':
                return ConcreteProductA()
            if some_property == 'b':
                return ConcreteProductB()
            if some_property == 'c':
                return ConcreteProductC()
            raise Exception('Class not found')
        except Exception as _e:
            print(_e)
        return None
