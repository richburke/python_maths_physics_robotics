import os
import sys
import math
from maths.arithmetic.utils import squared
from maths.geometry.defines import RightTriangleLeg, RightTriangleFields
sys.path.extend([os.getcwd()])


def make_right_triangle(opposite=None, adjacent=None, hypotenuse=None, opposite_angle=None, adjacent_angle=None, hypotenuse_angle=None):
    return {
        RightTriangleFields.OPPOSITE: opposite,
        RightTriangleFields.ADJACENT: adjacent,
        RightTriangleFields.HYPOTENUSE: hypotenuse,
        RightTriangleFields.OPPOSITE_ANGLE: opposite_angle,
        RightTriangleFields.ADJACENT_ANGLE: adjacent_angle,
    }

def triangle_remaining_angle(angle1, angle2):
    return 180 - angle1 - angle2

def right_triangle_remaining_angle(angle):
    return 90 - angle

def euclidean_distance(v1, v2):
    return math.sqrt(squared(v1) + squared(v2))

# Expects a right triangle dictionary with angle values in degrees.
def right_triangle_values_from_angle_leg(triangle, leg=RightTriangleLeg.OPPOSITE):
    opposite_angle = triangle[RightTriangleFields.OPPOSITE_ANGLE]
    adjacent_angle = right_triangle_remaining_angle(opposite_angle)

    if leg == RightTriangleLeg.ADJACENT:
        adjacent_leg = triangle[RightTriangleFields.ADJACENT]
        opposite_leg = adjacent_leg / math.cos(math.radians(opposite_angle)) * math.sin(math.radians(opposite_angle))
        hypothenuse = adjacent_leg / math.cos(math.radians(opposite_angle))
    else:
        opposite_leg = triangle[RightTriangleFields.OPPOSITE]
        adjacent_leg = opposite_leg / math.sin(math.radians(opposite_angle)) * math.cos(math.radians(opposite_angle))
        hypothenuse = opposite_leg / math.sin(math.radians(opposite_angle))

    return make_right_triangle(
        opposite=opposite_leg,
        adjacent=adjacent_leg,
        hypotenuse=hypothenuse,
        opposite_angle=opposite_angle,
        adjacent_angle=adjacent_angle
    )


    