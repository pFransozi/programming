"A director class"
from house_builder import HouseBuilder

class IglooDirector():
    "One of the directors, that can build a complex representations."

    @staticmethod
    def  construct():
        '''Note that in this IglooDirector, it has omitted the 
        set_number_windows call since this Igloo will have no
        windows. '''

        return HouseBuilder()\
            .set_building_type('Igloo') \
            .set_wall_material('Ice') \
            .set_number_doors(1)\
            .get_result()