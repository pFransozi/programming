from abc import ABCMeta, abstractmethod

class IBuilder (metaclass = ABCMeta):
    "The builder interface"

    @staticmethod
    @abstractmethod
    def build_part_a():
        "Build part a"
    
    @staticmethod
    @abstractmethod
    def build_part_b():
        "Build part b"
    
    @staticmethod
    @abstractmethod
    def build_part_c():
        "Build part c"
    

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"
    
class Builder(IBuilder):
    "Concrete builder"

    def __init__(self):
        self.product = Product()
    
    def build_part_a(self):
        self.product.parts.append('a')
        return self
    
    def build_part_b(self):
        self.product.parts.append('b')
        return self
    
    def build_part_c(self):
        self.product.parts.append('c')
        return self
    
    def get_result(self):
        return self.product

class Product():
    "The Product"

    def __init__(self):
        self.parts = []

class Director:
    "The director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and return the final product"

        return Builder() \
            .build_part_a() \
            .build_part_b() \
            .build_part_c() \
            .get_result()

# The Client
PRODUCT = Director().construct()
print(PRODUCT.parts)
