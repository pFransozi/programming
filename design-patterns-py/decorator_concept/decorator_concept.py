from abc import ABCMeta, abstractmethod

class IComponent(metaclass=ABCMeta):
    "methods the component must implment"

    @staticmethod
    @abstractmethod
    def method():
        "a method to implement"

class Component(IComponent):
    "a component that can be decorated or not"

    def method(self):
        "an example method"
        return "Componet method"

class Component1(IComponent):
    "a component 1 that cna be decorated or not"

    def method(self):
        "an example method"
        return "Component 1 method"

class Decorator(IComponent):
    "The decorator also implements the IComponent"

    def __init__(self, obj):
        "Set a reference to the decorated object"
        self.object = obj

    def method(self):
        "A method to implement"
        return f"Decorator Method({self.object.method()})"


# the client
COMPONENT = Component1()
print(COMPONENT.method())
print(Decorator(COMPONENT).method())

