from small_chair import SmallChair
from medium_chair import MediumChair
from big_chair import BigChair

class ChairFactory:

    @staticmethod
    def get_chair(chair):

        try:
            if chair == 'BigChair':
                return BigChair()
            if chair == 'MediumChair':
                return MediumChair()
            if chair == 'SmallChair':
                return SmallChair()

            raise Exception('Chair Not found.')
        except Exception as _e:
            print(_e)
        return None
