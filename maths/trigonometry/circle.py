import os
import sys
from maths.trigonometry.defines import PI, TWO_PI, QuadrantLocation

sys.path.extend([os.getcwd()])

def arc_length(radius):
    def fn(angle):
        return radius * angle
    return fn

def radian_length_from_circumference(circumference):
    return circumference / TWO_PI
