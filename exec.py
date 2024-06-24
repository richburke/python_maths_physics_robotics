#!/usr/bin/env python3
import math
from maths.arithmetic.utils import integers_within_interval
from maths.algebra.functions import is_function_even, is_function_odd
from maths.geometry.defines import RightTriangleLeg, RightTriangleFields
from maths.geometry.circles import radius_from_origin_and_point
from maths.geometry.angles import make_right_triangle, right_triangle_values_from_angle_leg, triangle_remaining_angle, euclidean_distance
from maths.trigonometry.defines import PI, PI_OVER_TWO, THREE_PI_OVER_TWO, QuadrantLocation
from maths.trigonometry.angles import degrees_to_radians, radians_to_degrees, to_principal_interval, to_positive_angle, to_negative_angle, number_of_full_rotations, angle_from_xy
from maths.trigonometry.identities import values_from, sin_cos, cos_sec, quadrants_of_cosecant, sin_csc
from maths.trigonometry.unit_circle import display_common_unit_circle_coordinates, coterminal_angles_within_interval, reference_angle

def main(args=None):
    source = make_right_triangle(adjacent=4, opposite_angle=35)
    print(right_triangle_values_from_angle_leg(source, RightTriangleLeg.ADJACENT))

    # print(-2 * math.sqrt(5) / 5, 4 * math.sqrt(5) / 5)

    # print(unit_circle_angles_of_sine(math.sin(math.radians(60))))
    # print(y)
    # print(degrees_to_radians(60), degrees_to_radians(300), degrees_to_radians(30), degrees_to_radians(330), degrees_to_radians(120), degrees_to_radians(150))
    # print(to_principal_interval(-75 * PI / 8), to_principal_interval(-75 * PI / 8) + 2 * PI)
    # print(quadrants_of_cosecant(quadrants_of_cosecant(y[1])))

if __name__ == "__main__":
    main()