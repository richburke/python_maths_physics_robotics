#!/usr/bin/env python3
import math
from maths.trigonometry.defines import PI_OVER_TWO, THREE_PI_OVER_TWO, QuadrantLocation
from maths.trigonometry.angles import degrees_to_radians, to_principal_interval, to_positive_angle, to_negative_angle, number_of_full_rotations
from maths.trigonometry.identities import values_from

def main(args=None):
    v1 = to_positive_angle(7 * math.pi / 3)
    v2 = to_positive_angle(25 * math.pi / 6)
    print(to_principal_interval(v1), to_principal_interval(v2))

    print(number_of_full_rotations(v1), number_of_full_rotations(v2))

    print(PI_OVER_TWO)
    a = math.pi
    a_prime = to_principal_interval(a)
    x = values_from(a)
    # x = values_from_cosine(QuadrantLocation.I)(v1)
    print(x, a_prime)
    # print(THREE_PI_OVER_TWO)

    # v = math.sqrt(42)/6
    # print(v)

if __name__ == "__main__":
    main()