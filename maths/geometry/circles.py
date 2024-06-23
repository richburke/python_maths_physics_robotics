import os
import sys
import math

sys.path.extend([os.getcwd()])

def radius_from_origin_and_point(h=0, k=0):
    def fn(x, y):
        return math.sqrt(pow(x - h, 2) + pow(y - k, 2))
    return fn