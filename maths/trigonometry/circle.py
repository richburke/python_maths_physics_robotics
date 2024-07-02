import os
import sys
from maths.arithmetic.utils import squared
from maths.trigonometry.defines import PI, TWO_PI, QuadrantLocation

sys.path.extend([os.getcwd()])

def arc_length(radius):
    def fn(angle):
        return radius * angle
    return fn

def radian_length_from_circumference(circumference):
    return circumference / TWO_PI

def revolutions_to_radians(revolutions):
    return revolutions * TWO_PI

def radians_to_revolutions(radians):
    return radians / TWO_PI

def sector_area(radius):
    def fn(angle):
        return 1 / 2 * squared(radius) * angle
    return fn
