"Bridge Pattern Concept Sample Code"

from abc import ABCMeta, abstractmethod

class IAbstraction(metaclass=ABCMeta):
    "The abstraction interface"


    @staticmethod
    @abstractmethod
    def method(*args):
        "The method handle"

class RefinedAbstractionA(IAbstraction):
    'A refined Abstraction'

    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(*args)

class RefinedAbstractionB(IAbstraction):

    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(*args)

class IImplementer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def method(*args:tuple) -> None:
        "The method implementation"

class ConcreteImplementerA(IImplementer):
    "A concrete Implementer"

    @staticmethod
    def method(*args:tuple) -> None:
        print(args)

class ConcreteImplementerB(IImplementer):

    @staticmethod
    def method(*args:tuple) -> None:
        for arg in args:
            print(arg)



# the client
REF_ABSTRACT_A = RefinedAbstractionA(ConcreteImplementerA)
REF_ABSTRACT_A.method('a', 'b', 'c')

REF_ABSTRACT_B = RefinedAbstractionB(ConcreteImplementerB)
REF_ABSTRACT_B.method('1', '2', '3')

REF_ABSTRACT_C = RefinedAbstractionB(ConcreteImplementerA)
REF_ABSTRACT_C.method('x', 'y', 'z')