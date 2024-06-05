import os
import sys
from maths.arithmetic.defines import EPSILON

sys.path.extend([os.getcwd()])

def sign_factor(value):
    return -1 if value < 0 else 1

def is_within_bounds(value, epsilon=EPSILON):
    return True if value <= epsilon and value >= -1* epsilon else False

# Parameter order is deliberate to allow a functional style.
def div(denominator, undef = None):
    def fn(numerator):
        if denominator == 0:
            return undef
        return numerator / denominator
    return fn

