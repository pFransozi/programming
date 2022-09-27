from interface_chair import IChair

class SmallChair(IChair):

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        return {
            "width": self._width,
            "height": self._height,
            "depth": self._depth
        }