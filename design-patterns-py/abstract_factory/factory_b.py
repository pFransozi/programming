from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object():
        "an abstract interface method"


class ConcreteProductA(IProduct):

    def __init__(self):
        self.name = 'ConcreteProductA'

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

    def create_object(self):
        return self

class FactoryB():

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