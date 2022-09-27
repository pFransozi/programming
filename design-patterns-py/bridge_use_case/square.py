from interface_shape import IShape

class Square(IShape):

    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_implementation()