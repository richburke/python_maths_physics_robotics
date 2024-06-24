import os
import sys
import math
from enum import Enum, IntEnum

sys.path.extend([os.getcwd()])

class RightTriangleLeg(IntEnum):
    OPPOSITE = 1
    ADJACENT = 2
    HYPOTENUSE = 3

class RightTriangleFields(Enum):
    OPPOSITE = "opposite"
    ADJACENT = "adjacent"
    HYPOTENUSE = "hypotenuse"
    OPPOSITE_ANGLE = "opposite_angle"
    ADJACENT_ANGLE = "adjacent_angle"