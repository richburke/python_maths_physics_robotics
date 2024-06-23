import os
import sys
import math
from tabulate import tabulate
from maths.arithmetic.defines import EPSILON
from maths.arithmetic.utils import div
from maths.trigonometry.defines import PI, TWO_PI, QuadrantLocation
from maths.arithmetic.utils import sign_factor, is_within_bounds

sys.path.extend([os.getcwd()])

'''
For character codes, [shift]+[control]+U, then continuing to hold
[shift]+[control], type the hex code.
π = 03C0
° = 00B0
θ = 03B8
'''


def display_common_angle_names():
    headers=['Angle', 'Degrees', 'Radians (π)', 'Radians (~#)']
    values=[
        ['0° or Zero', '0', '0', '0'],
        ['Acute', '0 < θ < 90', '0 < θ < π/2', '0 < θ < 1.57'],
        ['Right', '90', 'π/2', '1.57'],
        ['Obtuse', '90 < θ < 180', 'π/2 < θ < π', '1.57 < θ < 3.14'],
        ['Straight', '180', 'π', '3.14'],
        ['Reflex', '180 < θ < 360', 'π < θ < 2π', '3.14 < θ < 6.28'],
        ['360° or Complete', '360', '2π', '6.28'],
    ]
    colalign=['left', 'right', 'right', 'right']
    print(tabulate(values, headers=headers, colalign=colalign))

def display_common_angle_locations():
    headers=['Degrees', 'Radians (π)', 'Radians (~#)', 'Location']
    values=[
        ['0', '0', '0', 'Positive horizontal axis'],
        ['30', 'π/6', '{:.3f}'.format(PI / 6), '1st quadrant'],
        ['45', 'π/4', '{:.3f}'.format(PI / 4), '1st quadrant'],
        ['60', 'π/3', '{:.3f}'.format(PI / 3), '1st quadrant'],
        ['90', 'π/2', '{:.3f}'.format(PI / 2), 'Positive vertical axis'],
        ['120', '2π/3', '{:.3f}'.format(2 * PI / 3), '2nd quadrant'],
        ['135', '3π/4', '{:.3f}'.format(3 * PI / 4), '2nd quadrant'],
        ['150', '5π/6', '{:.3f}'.format(5 * PI / 6), '2nd quadrant'],
        ['180', 'π', '{:.3f}'.format(PI), 'Negative horizontal axis'],
        ['210', '7π/6', '{:.3f}'.format(7 * PI / 6), '3rd quadrant'],
        ['225', '5π/4', '{:.3f}'.format(5 * PI / 4), '3rd quadrant'],
        ['240', '4π/3', '{:.3f}'.format(4 * PI / 3), '3rd quadrant'],
        ['270', '3π/2', '{:.3f}'.format(3 * PI / 2), 'Negative vertical axis'],
        ['300', '5π/3', '{:.3f}'.format(5 * PI / 3), '4th quadrant'],
        ['315', '7π/4', '{:.3f}'.format(7 * PI / 4), '4th quadrant'],
        ['330', '11π/6', '{:.3f}'.format(11 * PI / 6), '4th quadrant'],
        ['360', '2π', '{:.3f}'.format(2 * PI), 'Positive horizontal axis'],
    ]
    colalign=['right', 'right', 'right', 'left']
    print(tabulate(values, headers=headers, colalign=colalign))

def radians_to_pi(value):
    return value / PI

def radians_to_degrees(value):
    return value * 180 / PI

def degrees_to_radians(value):
    return value * PI / 180

# Value in radians
def is_in_principal_interval(value):
    if value < 0:
        return True if value <= 0 and value >= -2 * PI else False
    return True if value >= 0 and value <= 2 * PI else False

# Value in radians
def to_principal_interval(value):
    sign = sign_factor(value)
    reduced = value / TWO_PI
    frac, whole = math.modf(reduced)
    # Cases in which the supplied angle is coterminal with 2π
    if whole != 0.0 and frac == 0.0:
        return sign * TWO_PI
    return frac * TWO_PI # "frac" retains the sign

# Value in radians
def are_coterminal(value1, value2, epsilon=EPSILON):
    diff = abs(to_principal_interval(value2 - value1))
    print(diff, value1, value2)
    if is_within_bounds(diff, epsilon):
        return True
    if is_within_bounds(diff - TWO_PI, epsilon):
        return True
    return False

# Parameter "value" is in radians
def number_of_full_rotations(value):
    if value < 0 and value > -TWO_PI:
        return 0
    if value >= 0 and value < TWO_PI:
        return 0
    _, whole = math.modf(value / TWO_PI)
    return int(whole)

def to_positive_angle(value):
    if value < 0:
        return value + TWO_PI + (TWO_PI * number_of_full_rotations(abs(value)))
    return value

def to_negative_angle(value):
    if value > 0:
        return value - TWO_PI - (TWO_PI * number_of_full_rotations(value))
    return value

def standardize_angle(value):
    if value < 0:
        value = to_positive_angle(value)
    if not is_in_principal_interval(value):
        value = to_principal_interval(value)
    return value

def quadrant_location_of_angle(value):
    value = standardize_angle(value)
    if value == PI / 2:
        return QuadrantLocation.YPositive
    if value == PI:
        return QuadrantLocation.XNegative
    if value == 3 * PI / 2:
        return QuadrantLocation.YNegative
    if value < PI / 2:
        return QuadrantLocation.I
    if value < PI:
        return QuadrantLocation.II
    if value < 3 * PI / 2:
        return QuadrantLocation.III
    if value < 2 * PI:
        return QuadrantLocation.IV
    return QuadrantLocation.XPositive

def quadrant_location_of_point(point):
    x, y = point
    if x == 0 and y == 0:
        return QuadrantLocation.Origin
    if x == 0 and y > 0:
        return QuadrantLocation.YPositive
    if x == 0 and y < 0:
        return QuadrantLocation.YNegative
    if x > 0 and y == 0:
        return QuadrantLocation.XPositive
    if x < 0 and y == 0:
        return QuadrantLocation.XNegative
    if x > 0 and y > 0:
        return QuadrantLocation.I
    if x < 0 and y > 0:
        return QuadrantLocation.II
    if x < 0 and y < 0:
        return QuadrantLocation.III
    if x > 0 and y < 0:
        return QuadrantLocation.IV
    return QuadrantLocation.XPositive

def angles_of_sine(value):
    angle = math.asin(value)
    return (angle, PI - angle)

def angles_of_cosine(value):
    angle = math.acos(value)
    return (angle, TWO_PI - angle)

def sine_from_xy(point):
    x, y = point
    return div(math.sqrt(pow(x, 2) + pow(y, 2)))(y)

def cosine_from_xy(point):
    x, y = point
    return div(math.sqrt(pow(x, 2) + pow(y, 2)))(x)

def angle_from_xy(point):
    x, y = point
    quadrant = quadrant_location_of_point(point)
    angle1, angle2 = angles_of_sine(sine_from_xy(point))
    quadrant_angle2 = quadrant_location_of_angle(angle2)
    if quadrant == quadrant_angle2:
        return angle2
    return angle1