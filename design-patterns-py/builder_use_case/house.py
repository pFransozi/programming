"The Product"

class House():
    "Product"

    def __init__(self, building_type="Apartment", doors=0, 
                windows=0, wall_material="Brick"):
        
        #brick, wood, straw, ice
        self.wall_material = wall_material
        
        #Apartment, Bungalow, Caravan, Hut, Castle, Duples, 
        # Houseboat, Igloo
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def construction(self):
        "Returns a string describing the constrction"

        return f"This is a {self.wall_material} " \
                f"{self.building_type} with {self.doors} " \
                f"door(s) and {self.windows} window(s)."

