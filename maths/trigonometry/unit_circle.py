import os
import sys
import math
from tabulate import tabulate
from maths.arithmetic.utils import div, is_within_interval, integers_within_interval
from maths.trigonometry.defines import PI, PI_OVER_TWO, TWO_PI, THREE_PI_OVER_TWO, Quadrant, QuadrantLocation
from maths.trigonometry.angles import number_of_full_rotations, quadrant_location_of_angle, standardize_angle
from maths.trigonometry.identities import sin_cos, cot_to_csc, csc_to_cot, cos_tan_to_sin, cos_cot_to_sin, quadrants_of_cosine

sys.path.extend([os.getcwd()])

'''
For character codes, [shift]+[control]+U, then continuing to hold
[shift]+[control], type the hex code.
π = 03C0
° = 00B0
θ = 03B8
√ = 221A
≈ = 2248
'''

def display_common_unit_circle_coordinates():
    headers=['Degrees', 'Radians (π)', 'Radians (~#)', 'X (cosine)', 'Y (sine)', 'Tangent']
    values=[
        ['0', '0', '0', '1', '0', '0'],
        ['15', 'π/12', '{:.3f}'.format(math.pi / 12), '(√6+√2)/4≈{:.3f}'.format(math.cos(math.pi / 12)), '(√6-√2)/4≈'+'{:.3f}'.format(math.sin(math.pi / 12)), '{:.3f}'.format(math.tan(math.pi / 12))],
        ['30', 'π/6', '{:.3f}'.format(math.pi / 6), '√3/2≈{:.3f}'.format(math.cos(math.pi / 6)), '1/2={:.3f}'.format(math.sin(math.pi / 6)), '{:.3f}'.format(math.tan(math.pi / 6))],
        ['45', 'π/4', '{:.3f}'.format(math.pi / 4), '√2/2≈{:.3f}'.format(math.cos(math.pi / 4)), '√2/2≈{:.3f}'.format(math.sin(math.pi / 4)), '{:.3f}'.format(math.tan(math.pi / 4))],
        ['60', 'π/3', '{:.3f}'.format(math.pi / 3), '1/2={:.3f}'.format(math.cos(math.pi / 3)), '√3/2≈{:.3f}'.format(math.sin(math.pi / 3)), '{:.3f}'.format(math.tan(math.pi / 3))],
        ['75', '5π/12', '{:.3f}'.format(5 * math.pi / 12), '(√6-√2)/4≈{:.3f}'.format(math.cos(5 * math.pi / 12)), '(√6+√2)/4≈{:.3f}'.format(math.sin(5 * math.pi / 12)), '{:.3f}'.format(math.tan(5 * math.pi / 12))],
        ['90', 'π/2', '{:.3f}'.format(math.pi / 2), '0', '1', 'undefined'],
        ['105', '7π/12', '{:.3f}'.format(7 * math.pi / 12), '-(√6-√2)/4≈{:.3f}'.format(math.cos(7 * math.pi / 12)), '(√6+√2)/4≈{:.3f}'.format(math.sin(7 * math.pi / 12)), '{:.3f}'.format(math.tan(7 * math.pi / 12))],
        ['120', '2π/3', '{:.3f}'.format(2 * math.pi / 3), '-1/2={:.3f}'.format(math.cos(2 * math.pi / 3)), '√3/2≈{:.3f}'.format(math.sin(2 * math.pi / 3)), '{:.3f}'.format(math.tan(2 * math.pi / 3))],
        ['135', '3π/4', '{:.3f}'.format(3 * math.pi / 4), '-√2/2≈{:.3f}'.format(math.cos(3 * math.pi / 4)), '√2/2≈{:.3f}'.format(math.sin(3 * math.pi / 4)), '{:.3f}'.format(math.tan(3 * math.pi / 4))],
        ['150', '5π/6', '{:.3f}'.format(5 * math.pi / 6), '-√3/2≈{:.3f}'.format(math.cos(5 * math.pi / 6)), '1/2={:.3f}'.format(math.sin(5 * math.pi / 6)), '{:.3f}'.format(math.tan(5 * math.pi / 6))],
        ['165', '11π/12', '{:.3f}'.format(11 * math.pi / 12), '-(√6+√2)/4≈{:.3f}'.format(math.cos(11 * math.pi / 12)), '(√6-√2)/4≈{:.3f}'.format(math.sin(11 * math.pi / 12)), '{:.3f}'.format(math.tan(11 * math.pi / 12))],
        ['180', 'π', '{:.3f}'.format(math.pi), '-1', '0', '0'],
        ['195', '13π/12', '{:.3f}'.format(13 * math.pi / 12), '-(√6+√2)/4≈{:.3f}'.format(math.cos(13 * math.pi / 12)), '-(√6-√2)/4≈{:.3f}'.format(math.sin(13 * math.pi / 12)), '{:.3f}'.format(math.tan(13 * math.pi / 12))],
        ['210', '7π/6', '{:.3f}'.format(7 * math.pi / 6), '-√3/2≈{:.3f}'.format(math.cos(7 * math.pi / 6)), '-1/2={:.3f}'.format(math.sin(7 * math.pi / 6)), '{:.3f}'.format(math.tan(7 * math.pi / 6))],
        ['225', '5π/4', '{:.3f}'.format(5 * math.pi / 4), '-√2/2≈{:.3f}'.format(math.cos(5 * math.pi / 4)), '-√2/2≈{:.3f}'.format(math.sin(5 * math.pi / 4)), '{:.3f}'.format(math.tan(5 * math.pi / 4))],
        ['240', '4π/3', '{:.3f}'.format(4 * math.pi / 3), '-1/2={:.3f}'.format(math.cos(4 * math.pi / 3)), '-√3/2≈{:.3f}'.format(math.sin(4 * math.pi / 3)), '{:.3f}'.format(math.tan(4 * math.pi / 3))],
        ['255', '17π/12', '{:.3f}'.format(17 * math.pi / 12), '-(√6-√2)/4≈{:.3f}'.format(math.cos(17 * math.pi / 12)), '-(√6+√2)/4≈{:.3f}'.format(math.sin(17 * math.pi / 12)), '{:.3f}'.format(math.tan(17 * math.pi / 12))],
        ['270', '3π/2', '{:.3f}'.format(3 * math.pi / 2), '0', '-1', 'undefined'],
        ['285', '19π/12', '{:.3f}'.format(19 * math.pi / 12), '(√6-√2)/4≈{:.3f}'.format(math.cos(19 * math.pi / 12)), '-(√6+√2)/4≈{:.3f}'.format(math.sin(19 * math.pi / 12)), '{:.3f}'.format(math.tan(19 * math.pi / 12))],
        ['300', '5π/3', '{:.3f}'.format(5 * math.pi / 3), '1/2={:.3f}'.format(math.cos(5 * math.pi / 3)), '-√3/2≈{:.3f}'.format(math.sin(5 * math.pi / 3)), '{:.3f}'.format(math.tan(5 * math.pi / 3))],
        ['315', '7π/4', '{:.3f}'.format(7 * math.pi / 4), '√2/2≈{:.3f}'.format(math.cos(7 * math.pi / 4)), '-√2/2≈{:.3f}'.format(math.sin(7 * math.pi / 4)), '{:.3f}'.format(math.tan(7 * math.pi / 4))],
        ['330', '11π/6', '{:.3f}'.format(11 * math.pi / 6), '√3/2≈{:.3f}'.format(math.cos(11 * math.pi / 6)), '-1/2={:.3f}'.format(math.sin(11 * math.pi / 6)), '{:.3f}'.format(math.tan(11 * math.pi / 6))],
        ['345', '23π/12', '{:.3f}'.format(23 * math.pi / 12), '(√6+√2)/4≈{:.3f}'.format(math.cos(23 * math.pi / 12)), '-(√6-√2)/4≈{:.3f}'.format(math.sin(23 * math.pi / 12)), '{:.3f}'.format(math.tan(23 * math.pi / 12))],
        ['360', '2π', '{:.3f}'.format(2 * math.pi), '1', '0', '0'],
    ]
    colalign=['right', 'right', 'right', 'right', 'right', 'right']
    print(tabulate(values, headers=headers, colalign=colalign))

def reference_angle(angle):
    angle = standardize_angle(angle)
    quadrant_location = quadrant_location_of_angle(angle)
    if quadrant_location == QuadrantLocation.II:
        return math.pi - angle
    if quadrant_location == QuadrantLocation.III:
        return angle - math.pi
    if quadrant_location == QuadrantLocation.IV:
        return TWO_PI - angle
    return angle

def coterminal_angles_within_interval(lower_bound, upper_bound):
    lower_bound_value, lower_bound_inclusive = lower_bound
    upper_bound_value, upper_bound_inclusive = upper_bound

    def fn(angle):
        if is_within_interval(lower_bound, upper_bound)(angle):
            rotations = number_of_full_rotations(upper_bound_value - lower_bound_value)
            a = []
            for i in range(rotations):
                a.append(angle + i * TWO_PI)
            return a
        
        updated_lower_bound_value = (lower_bound_value - angle) / TWO_PI
        updated_upper_bound_value = (upper_bound_value - angle) / TWO_PI
        integers = integers_within_interval((updated_lower_bound_value, lower_bound_inclusive), (updated_upper_bound_value, upper_bound_inclusive))

        a = []
        for integer in integers:
            a.append(angle + integer * TWO_PI)
        return a
    return fn
