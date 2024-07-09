#!/usr/bin/env python3
import math
from maths.arithmetic.utils import integers_within_interval
from maths.arithmetic.conversions import inches_to_centimeters, centimeters_to_inches, feet_to_miles
from maths.algebra.functions import is_function_even, is_function_odd
from maths.geometry.defines import RightTriangleLeg, RightTriangleFields
from maths.geometry.circle import radius_from_origin_and_point
from maths.geometry.triangle import make_right_triangle, right_triangle_values_from_angle_leg, right_triangle_remaining_angle, euclidean_distance, adjacent_leg_from_right_triangle, hypotenuse_from_right_triangle, opposite_leg_from_right_triangle
from maths.trigonometry.defines import PI, TWO_PI, PI_OVER_TWO, THREE_PI_OVER_TWO, QuadrantLocation, TrigFunction
from maths.trigonometry.angle import degrees_to_radians, radians_to_degrees, to_principal_interval, to_positive_angle, to_negative_angle, number_of_full_rotations, angle_from_xy, angle_after_rotations
from maths.trigonometry.identities import values_from, secant_from_values, cotangent_from_values
from maths.trigonometry.unit_circle import coterminal_angles_within_interval, display_common_unit_circle_coordinates
from maths.trigonometry.circle import sector_area, revolutions_to_radians
from physics.velocity import linear_velocity, angular_velocity, angular_velocity_from_revolutions_per_minute, linear_velocity_from_angular_velocity, angular_velocity_from_linear_velocity, angular_velocity_from_revolutions_per_second
from maths.trigonometry.graphing import plot_sine, plot_cosine, plot_sine_with_unscaled, plot_cosine_with_unscaled, plot_cosecant_with_unscaled, plot_cosecant, plot_secant, plot_secant_with_unscaled, period, amplitude


from matplotlib import pyplot as plt
import numpy as np

def main(args=None):
    
    # x = angular_velocity_from_revolutions_per_second(4) * 60 * 60
    # # y = x * 60
    # # z = y / TWO_PI
    # radius = 1.25
    # velocity = linear_velocity_from_angular_velocity(radius)(x)

    # print(feet_to_miles(velocity))
    # print(linear_velocity_from_angular_velocity(2.6)(9.4))
    # print(x, revolutions_per_second(x), " revolutions per second")
    # print(.620 * PI)
    # print(revolutions_per_minute(x), " revolutions per minute")

    # theta = np.linspace(-PI, 4 * PI)
    # plot_secant_with_unscaled(theta)(-2)

    p = period(TrigFunction.SINE)(PI ** 2)
    print(p, 2 / PI)
    p = period(TrigFunction.TANGENT)(4/3)
    print(p, 3 * PI / 4)
    p = period(TrigFunction.SECANT)(1/3)
    print(p, 6 * PI)
    p = period(TrigFunction.COTANGENT)(4 * PI / 3)
    print(p, 3 / 2)


    # display_common_unit_circle_coordinates()
    # plot_cosecant_with_unscaled(theta)()
    # plot_sine_wave_with_unscaled(theta)(2, 1/2)
    # plot_sine_wave_with_unscaled(theta)(1/2)
    # plot_cosine_wave_with_unscaled(theta)(2, 2)


    # xs = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    # ys = [16, 9, 4, 1, 0, 1, 4, 9, 16]
    # plt.scatter(xs, ys)

    # xs2 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    # ys2 = [-5, 1, 4, 5, 9, 11, 12, 13, 1]
    # plt.plot(xs2, ys2)

    # plt.show()
  
if __name__ == "__main__":
    main()