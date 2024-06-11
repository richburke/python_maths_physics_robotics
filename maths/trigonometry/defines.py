import os
import sys
import math
from enum import IntEnum

sys.path.extend([os.getcwd()])

PI_OVER_TWO = math.pi / 2
TWO_PI = math.pi * 2
THREE_PI_OVER_TWO = 3 * math.pi / 2

class TrigFunction(IntEnum):
    SINE = 1
    COSINE = 2
    TANGENT = 3
    COSECANT = 4
    SECANT = 5
    COTANGENT = 6

class Quadrant(IntEnum):
    I = 1
    II= 2
    III = 3
    IV = 4

class QuadrantLocation(IntEnum):
    Origin = 0
    I = 1
    II= 2
    III = 3
    IV = 4
    # QuadrantalAngles
    XPositive = 5
    YPositive = 6
    XNegative = 7
    YNegative = 8
