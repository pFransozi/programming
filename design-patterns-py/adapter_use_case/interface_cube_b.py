from abc import ABCMeta, abstractmethod

class ICubeB(metaclass=ABCMeta):
    "an interface for an object"

    @staticmethod
    @abstractmethod
    def create(top_left_front, bottom_right_back):
        "manufactures a cube with coords offset [0,0,0]"