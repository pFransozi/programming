class SubSystemClassA:
    "a hypothetically complicated class"

    @staticmethod
    def method():
        return 'A'

class SubSystemClassB:

    @staticmethod
    def method(value):
        return value

class SubSystemClassC:

    @staticmethod
    def method(value):
        return value

class Facade():

    @staticmethod
    def sub_system_class_a():
        return SubSystemClassA().method()

    @staticmethod
    def sub_system_class_b(value):
        return SubSystemClassB().method(value)

    @staticmethod
    def sub_system_class_c(value):
        return SubSystemClassC().method(value)


print(SubSystemClassA().method())
print(SubSystemClassB().method("B"))
print(SubSystemClassC().method({"C":[1, 2, 3]}))

print(Facade().sub_system_class_a())
print(Facade().sub_system_class_b("B"))
print(Facade().sub_system_class_c({"C":[1, 2, 3]}))