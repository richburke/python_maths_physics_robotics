#!/usr/bin/env python3
import math
from maths.arithmetic.utils import integers_within_interval
from maths.algebra.functions import is_function_even, is_function_odd
from maths.geometry.defines import RightTriangleLeg, RightTriangleFields
from maths.geometry.circles import radius_from_origin_and_point
from maths.geometry.triangles import make_right_triangle, right_triangle_values_from_angle_leg, right_triangle_remaining_angle, euclidean_distance, adjacent_leg_from_right_triangle, hypotenuse_from_right_triangle, opposite_leg_from_right_triangle
from maths.trigonometry.defines import PI, TWO_PI, PI_OVER_TWO, THREE_PI_OVER_TWO, QuadrantLocation
from maths.trigonometry.angles import degrees_to_radians, radians_to_degrees, to_principal_interval, to_positive_angle, to_negative_angle, number_of_full_rotations, angle_from_xy, angle_after_rotations, arc_length
from maths.trigonometry.identities import values_from, secant_from_values, cotangent_from_values
from maths.trigonometry.unit_circle import coterminal_angles_within_interval

def main(args=None):
    print(degrees_to_radians(252)) 
  
if __name__ == "__main__":
    main()