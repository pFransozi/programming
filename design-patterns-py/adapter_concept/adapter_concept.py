from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    "An interface from an object"
    
    @staticmethod
    @abstractmethod
    def method_a():
        "an abstract method A"

class ClassA(IA):
    "a sample class the implements IA"

    def method_a(self):
        print("method A")

class IB(metaclass=ABCMeta):
    "an interface for an object"

    @staticmethod
    @abstractmethod
    def method_b():
        "an abstract method b"

class ClassB(IB):
    "a sample class the implements IB"

    def method_b(self):
        print("method b")

class ClassBAdapter(IA):
    "Class b does not have a method_a, so we can create an adapter"

    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        "calls the class b method_b instead"
        self.class_b.method_b()

# the client
# before the adapter I need to test the objects class to know
# which method to call
ITEMS = [ClassA(), ClassB()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()

# after creating an adapter for ClassB I can reuse the same
# method signature as ClassA (preferred)
ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    item.method_a()