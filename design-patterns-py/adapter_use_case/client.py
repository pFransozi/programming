import time
import random
from cube_a import CubeA
from cube_b_adapter import CubeBAdapter

# client
TOTALCUBES = 5
COUNTER = 0

while COUNTER < TOTALCUBES:

    width = random.randint(1, 10)
    height = random.randint(1, 10)
    depth = random.randint(1, 10)

    cube = CubeA()
    success = cube.manufacture(width, height, depth)

    if success:
        print(
            f"Company A building Cube id:{id(cube)}, "
            f"{cube.width} x {cube.height} x {cube.depth}" )

        COUNTER += 1
    else: # try other manufacturer
        print('Company A is busy, trying company B')
        cube = CubeBAdapter()
        success = cube.manufacture(width, height, depth)

        if success:
            print(
                f"Company B building Cube id:{id(cube)}, "
                f"{cube.width} x {cube.height} x {cube.depth}")
            COUNTER += 1
        else:
            print('Company B is busy, trying company A')
    
    time.sleep(1)

print(f"{TOTALCUBES}")