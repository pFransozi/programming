"Prototype concept: sample code"
from abc import ABCMeta, abstractmethod

class IPrototype(metaclass=ABCMeta):
    "interface with clone method"

    @staticmethod
    @abstractmethod
    def clone():
        ''' The clone, deep or shallow, 
        it is up to you how you wnat to implement the
        details in your concrete class '''

class MyClass(IPrototype):
    "A concrete class"

    def __init__(self, field):
        self.field = field

    def clone(self):
        ''' this clone method uses a shallow copy
        technique '''

        return type(self)(
            self.field

            # a shallow copy is returned self.field.copy()
            # this is also a shallow copy, but has also
            # shallow copied the first level of the field.and
            # so it is essencially deep copy collections
            # containing inner collections, eg. lists of lists,
            # use https://docs.python.org/3/library/copy.html
            
            )

    def __str__(self):
        return f"{id(self)} \tfield={self.field}\t \
                    type={type(self.field)}"

#the client

OBJECT1 = MyClass([1, 2, 3, 4, 5]) # create the object containing list
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone()
OBJECT2.field[1] = 101

print(f"OBJECT1 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")