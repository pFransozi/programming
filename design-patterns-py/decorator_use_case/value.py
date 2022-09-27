from interface_value import IValue

class Value(IValue):
    "a component that can be decorated or not"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)