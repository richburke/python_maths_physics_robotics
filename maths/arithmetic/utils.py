import os
import sys
import math
from maths.arithmetic.defines import EPSILON

sys.path.extend([os.getcwd()]) 

def sign_factor(value):
    return -1 if value < 0 else 1

# Parameter order is deliberate to allow a functional style.
def div(denominator, undef = None):
    def fn(numerator):
        if denominator == 0:
            return undef
        return numerator / denominator
    return fn

def squared(v):
    return pow(v, 2)

def clamp(upper, lower=0):
    def fn(value):
        if value < lower:
            return lower
        if value > upper:
            return upper
        return value
    return fn

def integer_mantissa(value):
    f, i = math.modf(value)
    return (int(i),f)

def is_within_bounds(value, epsilon=EPSILON):
    return True if value <= epsilon and value >= -1* epsilon else False

def is_within_interval(lower_bound, upper_bound):
    lower_bound_value, lower_bound_inclusive = lower_bound
    upper_bound_value, upper_bound_inclusive = upper_bound

    def fn(value, epsilon=EPSILON):
        if lower_bound_inclusive:
            if value + epsilon < lower_bound_value:
                return False
        if not lower_bound_inclusive:
            if value + epsilon <= lower_bound_value:
                return False
        if upper_bound_inclusive:
            if value - epsilon > upper_bound_value:
                return False
        if not upper_bound_inclusive:
            if value - epsilon >= upper_bound_value:
                return False
        return True
    return fn

def integers_within_interval(lower_bound, upper_bound):
    a = []
    lower_bound_value, lower_bound_inclusive = lower_bound
    upper_bound_value, upper_bound_inclusive = upper_bound

    if upper_bound_value < lower_bound_value:
        return a

    lower_bound_integer, lower_bound_mantissa = integer_mantissa(lower_bound_value)
    upper_bound_integer, upper_bound_mantissa = integer_mantissa(upper_bound_value)

    if lower_bound_value < 0:
        start = lower_bound_integer + 1 if not lower_bound_inclusive and lower_bound_mantissa == 0.0 else lower_bound_integer
    else:
        start = lower_bound_integer + 1 if not lower_bound_inclusive or lower_bound_mantissa != 0.0 else lower_bound_integer

    if upper_bound_value <= 0:
        end = upper_bound_integer - 1 if not upper_bound_inclusive or upper_bound_mantissa != 0.0 else upper_bound_integer
    else:
        end = upper_bound_integer - 1 if not upper_bound_inclusive and upper_bound_mantissa == 0.0 else upper_bound_integer

    for k in range(start, end + 1):
        a.append(k)
    return a

