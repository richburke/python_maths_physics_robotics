#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
from maths.arithmetic.utils import asubtract, asquared_sum
# from maths.arithmetic.conversions import inches_to_centimeters, centimeters_to_inches, feet_to_miles
# from maths.algebra.functions import is_function_even, is_function_odd
# from maths.geometry.defines import RightTriangleLeg, RightTriangleFields
# from maths.geometry.circle import radius_from_origin_and_point
# from maths.geometry.triangle import make_right_triangle, right_triangle_values_from_angle_leg, right_triangle_remaining_angle, euclidean_distance, adjacent_leg_from_right_triangle, hypotenuse_from_right_triangle, opposite_leg_from_right_triangle
# from maths.trigonometry.defines import PI, TWO_PI, PI_OVER_TWO, THREE_PI_OVER_TWO, QuadrantLocation, TrigFunction
# from maths.trigonometry.angle import degrees_to_radians, radians_to_degrees, to_principal_interval, to_positive_angle, to_negative_angle, number_of_full_rotations, angle_from_xy, angle_after_rotations
# from maths.trigonometry.identities import values_from, secant_from_values, cotangent_from_values
# from maths.trigonometry.unit_circle import coterminal_angles_within_interval, display_common_unit_circle_coordinates
# from maths.trigonometry.circle import sector_area, revolutions_to_radians
# from physics.velocity import linear_velocity, angular_velocity, angular_velocity_from_revolutions_per_minute, linear_velocity_from_angular_velocity, angular_velocity_from_linear_velocity, angular_velocity_from_revolutions_per_second
# from maths.trigonometry.graphing import plot_tangent_with_unscaled, plot_cotangent, plot_cotangent_with_unscaled, adjacent_vertical_asympotes
# from external_samples.quadtree.quadtree_demo1 import quadtree_demo1
# from external_samples.quadtree.quadtree_demo2 import quadtree_demo2
from maths.statistics.defines import Mean
from maths.statistics.utils import mean
from maths.statistics.correlation import linear_regression, polynomial_regression_model, polynomial_regression, least_squares_regression, r_squared, standard_error_of_the_estimate


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

    # theta = np.linspace(-PI, 4 * PI, 1000)
    # plot_tangent_with_unscaled(theta)()
    # plot_tangent_with_unscaled(theta)(2, 2 / 3, 0, 0)
    # x = adjacent_vertical_asympotes(TrigFunction.COTANGENT)(1/2, 0)
    # print(x)
    # print('A', -PI, PI, 3 * PI)
    # print('B', 0, 2 * PI, 4 * PI)
    # print('C', 0, PI, 2 * PI)

    # quadtree_demo2()

    # display_common_unit_circle_coordinates()
    # plot_cosecant_with_unscaled(theta)()
    # plot_sine_wave_with_unscaled(theta)(2, 1/2)
    # plot_sine_wave_with_unscaled(theta)(1/2)
    # plot_cosine_wave_with_unscaled(theta)(2, 2)

    # plt.ioff()

    # m = np.array([[0.1, 1], [0.6, 1]])
    # n = np.array([0.1, 0.8])
    # inv = np.linalg.inv(m)
    # mm = np.matmul(inv, n)
    # print(mm)

    # xs = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    # ys = [16, 9, 4, 1, 0, 1, 4, 9, 16]
    xs = np.array([1, 2, 3, 4, 5])
    ys = np.array([2, 4, 5, 4, 5])

    axis = plt.gca()
    axis.set_xlim([0, 6])
    axis.set_ylim([0, 6])
    plt.scatter(xs, ys)

    x_mean = mean(Mean.ARITHMETIC)(xs)
    y_mean = mean(Mean.ARITHMETIC)(ys)
    plt.plot([x_mean, x_mean], [0, 6], color='red', linestyle='dashed')
    plt.plot([0, 6], [y_mean, y_mean], color='red', linestyle='dashed')

    xn = np.linspace(0, 6, 100)
    yn = linear_regression(xs)(ys)(xn)
    plt.plot(xn, yn, color='blue', linestyle='dashed')
    plt.show()

    # regressor = LinearRegression()
    # poly_features = PolynomialFeatures(degree=8, include_bias=False)

    xp = 4 * np.random.rand(100, 1) - 2
    yp = 4 + 2 * xp + 5 * xp ** 2 + 10 * np.random.randn(100, 1)

    # xn_poly = poly_features.fit_transform(xn)
    # regressor.fit(xn_poly, yn)

    # x_vals = np.linspace(-2, 2, 100).reshape(-1, 1)
    # x_vals_poly = poly_features.fit_transform(x_vals)
    # y_vals = regressor.predict(x_vals_poly)

    x_vals = np.linspace(-2, 2, 100)
    y_vals = polynomial_regression(2)(xp)(yp)(x_vals)

    # d = polynomial_regression_model(2)(xp)(yp)

    plt.scatter(xp, yp)
    plt.plot(x_vals, y_vals, color='gray', linestyle='dashed')
    plt.show()

    # print(r_squared(xs)(ys))
    # print(standard_error_of_the_estimate(xs)(ys))


if __name__ == "__main__":
    main()
