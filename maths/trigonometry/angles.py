import os
import sys
import math
from tabulate import tabulate

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

