import copy

class Singleton():
    "The singleton class"

    value = []

    def __new__(cls):
        return cls

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):
        "Use @classmethod to access class level variables"
        print(cls.value)


# the client
# all uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t={id(Singleton)}")
Singleton.value.append(1)

obj_1 = Singleton()
print(f"id(obj_1)\t={id(obj_1)}")
obj_1.value.append(2)

obj_2 = copy.deepcopy(obj_1)
print(f"id(obj_2)\t={id(obj_2)}")

obj_3 = Singleton()
print(f"id(obj_3)\t={id(obj_3)}")

print(obj_2.value)