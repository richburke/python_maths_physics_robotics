import os
import sys
import math
from maths.arithmetic.utils import div

sys.path.extend([os.getcwd()])

# Reciprocal identities
def sin_csc(value):
    if value == None:
        return 0
    return div(value)(1)

def cos_sec(value):
    if value == None:
        return 0
    return div(value)(1)

def tan_cot(value):
    if value == None:
        return 0
    return div(value)(1)

# Quotient identities
def sin_cos_to_tan(num, den):
    if den == None:
        return 0
    return div(den)(num)

def cos_sin_to_cot(cos, sin):
    if sin == None:
        return 0
    return div(sin)(cos)

# Pythagorean identities
def sin_cos(value):
    x = math.sqrt(1 - pow(value, 2))
    return (x, -1 * x)

def cot_to_csc(value):
    x = math.sqrt(pow(value, 2) + 1)
    return (x, -1 * x)

def csc_to_cot(value):
    x = math.sqrt(pow(value, 2) - 1)
    return (x, -1 * x)

# Derivations
def cos_tan_to_sin(cos, tan):
    if cos == None or tan == None:
        return None
    return cos * tan

def cos_cot_to_sin(cos, cot):
    if cot == None:
        return None
    return div(cot)(cos)

def sin_tan_to_cos(sin, tan):
    if tan == None:
        return None
    return div(tan)(sin)

def csc_cot_to_cos(csc, cot):
    if csc == None or cot == None:
        return None
    return cot * sin_csc(csc)

def tan_sec_to_sin(tan, sec):
    if sec == None:
        return None
    return tan * cos_sec(sec)

def sin_to_cot(sin):
    x = math.sqrt(pow(sin_csc(sin), 2) - 1)
    return (x, -1 * x)

def cos_to_tan(cos):
    sec = cos_sec(cos)
    if sec == None:
        return (None, None)
    x = math.sqrt(pow(sec, 2) - 1)
    return (x, -1 * x)