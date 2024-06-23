#!/usr/bin/env python3
import math
from maths.arithmetic.utils import integers_within_interval
from maths.algebra.functions import is_function_even, is_function_odd
from maths.geometry.circles import radius_from_origin_and_point
from maths.trigonometry.defines import PI, PI_OVER_TWO, THREE_PI_OVER_TWO, QuadrantLocation
from maths.trigonometry.angles import degrees_to_radians, radians_to_degrees, to_principal_interval, to_positive_angle, to_negative_angle, number_of_full_rotations, angle_from_xy
from maths.trigonometry.identities import values_from, sin_cos, cos_sec, quadrants_of_cosecant, sin_csc
from maths.trigonometry.unit_circle import display_common_unit_circle_coordinates, coterminal_angles_within_interval, reference_angle

def main(args=None):
    alpha = angle_from_xy((12, 5))
    theta = alpha + PI
    print(math.sin(theta), math.cos(theta))
    print('A', -5 /13, -12 / 13)
    print('B', -12/17, -5/17)
    print('C', 5 / 17, -12 / 17)
    print('D', 12/13, 5/13)
    # print(-2 * math.sqrt(5) / 5, 4 * math.sqrt(5) / 5)

    # print(unit_circle_angles_of_sine(math.sin(math.radians(60))))
    # print(y)
    # print(degrees_to_radians(60), degrees_to_radians(300), degrees_to_radians(30), degrees_to_radians(330), degrees_to_radians(120), degrees_to_radians(150))
    # print(to_principal_interval(-75 * PI / 8), to_principal_interval(-75 * PI / 8) + 2 * PI)
    # print(quadrants_of_cosecant(quadrants_of_cosecant(y[1])))

if __name__ == "__main__":
    main()