from circle_implementer import CircleImplementer
from square_implementer import SquareImplementer
from circle import Circle
from square import Square

CIRCLE = Circle(CircleImplementer)
CIRCLE.draw()
print()
print()
print()
SQUARE = Square(SquareImplementer)
SQUARE.draw()
print()
print()
print()
SQUARE = Square(CircleImplementer)
SQUARE.draw()