import os
import sys

sys.path.extend([os.getcwd()])


def slope_of_line_two_points(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def equation_of_line_two_points(p1, p2):
    m = slope_of_line_two_points(p1, p2)
    b = p1[1] - m * p1[0]
    return lambda x: m * x + b


def equation_of_line_slope_intercept(m, b):
    return lambda x: m * x + b
