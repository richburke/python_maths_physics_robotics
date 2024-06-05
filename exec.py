#!/usr/bin/env python3
import math
from maths.trigonometry.angles import are_coterminal, degrees_to_radians
from maths.trigonometry.identities import cos_to_tan

def main(args=None):
    # print(convert_radians_to_pi(4.0))
    # display_common_angle_locations()
    # print(are_coterminal((71 * math.pi)/16, (-25 * math.pi)/16))
    # print(are_coterminal(degrees_to_radians(-150), degrees_to_radians(210)))
    # print(are_coterminal(degrees_to_radians(-150), degrees_to_radians(570)))
    # print(-2.6179938779914944 + 6.28, 3.6651914291880923)
    v1 = -0.412
    # v2 = 17/15
    # x = sin_cos(v1)[0]
    # y = cos_sin_to_cot(x, v1)
    x = cos_to_tan(v1)[1]
    print(x)
    # print(sin_csc(sin_csc(v)))
    # print(v)
    # v = cos_sin_to_cot(1, v)
    # print(v)
    # v = cos_sin_to_cot(1, v)
    # print(v)

if __name__ == "__main__":
    main()