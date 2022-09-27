"A director class to build a houseboat product"
from house_builder import HouseBuilder

class HouseboatDirector: 
    '''One of the Director, that can build 
    a complex representations.'''

    @staticmethod
    def construct():

        "Construct and returns the final product"
        return HouseBuilder() \
            .set_building_type("Houseboat") \
            .set_wall_material("Wood") \
            .set_number_doors(6) \
            .set_number_windows(8) \
            .get_result()