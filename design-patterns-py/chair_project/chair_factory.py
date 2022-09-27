from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory:

    @staticmethod
    def get_chair(chair):

        if chair == 'B':
            return BigChair()
        if chair == 'M':
            return MediumChair()
        if chair == 'S':
            return SmallChair()
        
        return None