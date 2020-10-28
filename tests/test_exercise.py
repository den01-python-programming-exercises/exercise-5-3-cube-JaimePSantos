import pytest
import os

def test_exercise():
    os.chdir('src')

    from cube import Cube
    sand = Cube(3)

    assert sand.volume() == 27
    assert str(sand) == "The length of the edge is 3 and the volume 27"
