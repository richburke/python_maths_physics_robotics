#!/usr/bin/env python3

# π = [shift]+[control]+U then 03C0 (hold for both u and hex code)

from tabulate import tabulate

def display_angles_table():
    headers=['Type', 'Degrees', 'Radians (π)', 'Radians (~#)']
    values=[
        ['0 degree', '0', '0', '0'],
        ['Acute', '> 0, < 90', '> 0, < π/2', '> 0, < 1.57'],
        ['90 degree', '90', 'π/2', '1.57'],
        ['Obtuse', '> 90, < 180', '> π/2, < π', '> 1.57, < 3.14'],
        ['Straight', '180', 'π', '3.14'],
        ['Reflex', '> 180, < 360', '> π, < 2π', '> 3.14, < 6.28'],
        ['360 degree', '360', '2π', '6.28'],
    ]
    colalign=['left', 'right', 'right', 'right']
    print(tabulate(values, headers=headers, colalign=colalign))


def main(args=None):
    display_angles_table()


if __name__ == "__main__":
    main()