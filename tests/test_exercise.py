import pytest
import os
from src.cube import Cube
def test_exercise():
    os.chdir('src')

    sand = Cube(3)

    assert sand.volume() == 27
    assert str(sand) == "The length of the edge is 3 and the volume 27"
