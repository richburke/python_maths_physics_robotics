import os
import sys
import math
from tabulate import tabulate
from maths.arithmetic.defines import EPSILON
from maths.trigonometry.defines import TWO_PI, QuadrantLocation
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
        ['30', 'π/6', '{:.3f}'.format(math.pi / 6), '1st quadrant'],
        ['45', 'π/4', '{:.3f}'.format(math.pi / 4), '1st quadrant'],
        ['60', 'π/3', '{:.3f}'.format(math.pi / 3), '1st quadrant'],
        ['90', 'π/2', '{:.3f}'.format(math.pi / 2), 'Positive vertical axis'],
        ['120', '2π/3', '{:.3f}'.format(2 * math.pi / 3), '2nd quadrant'],
        ['135', '3π/4', '{:.3f}'.format(3 * math.pi / 4), '2nd quadrant'],
        ['150', '5π/6', '{:.3f}'.format(5 * math.pi / 6), '2nd quadrant'],
        ['180', 'π', '{:.3f}'.format(math.pi), 'Negative horizontal axis'],
        ['210', '7π/6', '{:.3f}'.format(7 * math.pi / 6), '3rd quadrant'],
        ['225', '5π/4', '{:.3f}'.format(5 * math.pi / 4), '3rd quadrant'],
        ['240', '4π/3', '{:.3f}'.format(4 * math.pi / 3), '3rd quadrant'],
        ['270', '3π/2', '{:.3f}'.format(3 * math.pi / 2), 'Negative vertical axis'],
        ['300', '5π/3', '{:.3f}'.format(5 * math.pi / 3), '4th quadrant'],
        ['315', '7π/4', '{:.3f}'.format(7 * math.pi / 4), '4th quadrant'],
        ['330', '11π/6', '{:.3f}'.format(11 * math.pi / 6), '4th quadrant'],
        ['360', '2π', '{:.3f}'.format(2 * math.pi), 'Positive horizontal axis'],
    ]
    colalign=['right', 'right', 'right', 'left']
    print(tabulate(values, headers=headers, colalign=colalign))

def radians_to_pi(value):
    return value / math.pi

def radians_to_degrees(value):
    return value * 180 / math.pi

def degrees_to_radians(value):
    return value * math.pi / 180

# Value in radians
def is_in_principal_interval(value):
    if value < 0:
        return True if value <= 0 and value >= -2 * math.pi else False
    return True if value >= 0 and value <= 2 * math.pi else False

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

# Value in radians
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

def quadrant_location_of_angle(value):
    if value < 0:
        value = to_positive_angle(value)

    if value == math.pi / 2:
        return QuadrantLocation.YPositive
    if value == math.pi:
        return QuadrantLocation.XNegative
    if value == 3 * math.pi / 2:
        return QuadrantLocation.YNegative
    if value < math.pi / 2:
        return QuadrantLocation.I
    if value < math.pi:
        return QuadrantLocation.II
    if value < 3 * math.pi / 2:
        return QuadrantLocation.III
    if value < 2 * math.pi:
        return QuadrantLocation.IV
    return QuadrantLocation.XPositive