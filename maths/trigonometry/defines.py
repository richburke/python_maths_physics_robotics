import os
import sys
from enum import IntEnum

sys.path.extend([os.getcwd()])

class Quadrant(IntEnum):
    I = 1
    II= 2
    III = 3
    IV = 4
    