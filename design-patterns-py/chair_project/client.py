from chair_factory import ChairFactory

CHAIR = ChairFactory().get_chair('M')
print(CHAIR.get_dimensions())