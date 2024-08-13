import os
import sys
import math
from enum import Enum, IntEnum

sys.path.extend([os.getcwd()])


class Mean(IntEnum):
    ARITHMETIC = 1
    QUADRATIC = 2
