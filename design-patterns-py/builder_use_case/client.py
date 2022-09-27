"House Builder Example Code"

from igloo_director import IglooDirector
from castle_director import CastleDirector
from houseboat_director import HouseboatDirector

IGLOO = IglooDirector().construct()
CASTLE = CastleDirector().construct()
HOUSEBOAT = HouseboatDirector().construct()

print(IGLOO.construction())
print(CASTLE.construction())
print(HOUSEBOAT.construction())