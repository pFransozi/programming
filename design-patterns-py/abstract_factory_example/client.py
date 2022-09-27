from furniture_factory import FurnitureFactory


FURNITURE = FurnitureFactory().get_furniture('SmallChair')
print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")