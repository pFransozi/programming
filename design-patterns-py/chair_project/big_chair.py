"A class of Chair"

from interface_chair import IChair

class BigChair(IChair):
    """The medium chair concrete class implements the
    IChair interface"""

    def __init__(self):
        self._height = 100
        self._width = 100
        self._depth = 100

    def get_dimensions(self):
        return {'width': self._width,
                'depth': self._depth,
                'height': self._height}
