from interface_table import ITable

class SmallTable(ITable):

    def __init__(self):
        self._height = 60
        self._width = 100
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }