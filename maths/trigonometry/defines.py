import os
import sys
import math
from enum import Enum, IntEnum

sys.path.extend([os.getcwd()])

PI = math.pi
PI_OVER_TWO = PI / 2
TWO_PI = PI* 2
THREE_PI_OVER_TWO = 3 * PI / 2
SQUARE_ROOT_OF_TWO = math.sqrt(2)
SQUARE_ROOT_OF_THREE = math.sqrt(3)

class TrigFunction(IntEnum):
    SINE = 1
    COSINE = 2
    TANGENT = 3
    COSECANT = 4
    SECANT = 5
    COTANGENT = 6

class TrigFunctionNames(Enum):
    SINE = "sine"
    COSINE = "cosine"
    TANGENT = "tangent"
    COSECANT = "cosecant"
    SECANT = "secant"
    COTANGENT = "cotangent"

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
