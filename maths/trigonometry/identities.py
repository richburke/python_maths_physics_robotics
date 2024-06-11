import os
import sys
import math
from maths.arithmetic.utils import div
from maths.trigonometry.defines import PI_OVER_TWO, TWO_PI, THREE_PI_OVER_TWO, Quadrant, QuadrantLocation
from maths.trigonometry.angles import quadrant_location_of_angle, to_principal_interval

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

def quadrants_of_sine(value):
    if value == 0 or value == None:
        return [Quadrant.I, Quadrant.II, Quadrant.III, Quadrant.IV]
    return [Quadrant.III, Quadrant.IV] if value < 0 else [Quadrant.I, Quadrant.II]

def quadrants_of_cosecant(value):
    if value == 0 or value == None:
        return [Quadrant.I, Quadrant.II, Quadrant.III, Quadrant.IV]
    return [Quadrant.III, Quadrant.IV] if value < 0 else [Quadrant.I, Quadrant.II]

def quadrants_of_cosine(value):
    if value == 0 or value == None:
        return [Quadrant.I, Quadrant.II, Quadrant.III, Quadrant.IV]
    return [Quadrant.II, Quadrant.III] if value < 0 else [Quadrant.I, Quadrant.IV]

def quadrants_of_secant(value):
    if value == 0 or value == None:
        return [Quadrant.I, Quadrant.II, Quadrant.III, Quadrant.IV]
    return [Quadrant.II, Quadrant.III] if value < 0 else [Quadrant.I, Quadrant.IV]

def quadrants_of_tangent(value):
    if value == 0 or value == None:
        return [Quadrant.I, Quadrant.II, Quadrant.III, Quadrant.IV]
    return [Quadrant.II, Quadrant.IV] if value < 0 else [Quadrant.I, Quadrant.III]

def quadrants_of_cotangent(value):
    if value == 0 or value == None:
        return [Quadrant.I, Quadrant.II, Quadrant.III, Quadrant.IV]
    return [Quadrant.II, Quadrant.IV] if value < 0 else [Quadrant.I, Quadrant.III]

def sign_of_sine_in_quadrant(quadrant):
    return -1 if quadrant in [Quadrant.III, Quadrant.IV] else 1

def sign_of_cosecant_in_quadrant(quadrant):
    return -1 if quadrant in [Quadrant.III, Quadrant.IV] else 1

def sign_of_cosine_in_quadrant(quadrant):
    return -1 if quadrant in [Quadrant.II, Quadrant.III] else 1 

def sign_of_secant_in_quadrant(quadrant):
    return -1 if quadrant in [Quadrant.II, Quadrant.III] else 1

def sign_of_tangent_in_quadrant(quadrant):
    return -1 if quadrant in [Quadrant.II, Quadrant.IV] else 1

def sign_of_cotangent_in_quadrant(quadrant):
    return -1 if quadrant in [Quadrant.II, Quadrant.IV] else 1

# Expand to include quadrantal angles
def _index_of_values(quadrant = Quadrant.I):
    index_sin_csc = 0 if quadrant in [Quadrant.I, Quadrant.II] else 1
    index_cos_sec = 0 if quadrant in [Quadrant.I, Quadrant.IV] else 1
    index_tan_cot = 0 if quadrant in [Quadrant.I, Quadrant.III] else 1
    return {
        "sine": index_sin_csc,
        "cosecant": index_sin_csc,
        "cosine": index_cos_sec,
        "secant": index_cos_sec,
        "tangent": index_tan_cot,
        "cotangent": index_tan_cot,
    }

def values_from(angle):
    quadrant_location = quadrant_location_of_angle(angle)
    principal_interval_angle = to_principal_interval(angle)

    if principal_interval_angle == 0 or principal_interval_angle == TWO_PI:
        return {
            "angle": angle,
            "principal_interval": principal_interval_angle,
            "quadrant": QuadrantLocation.XPositive,
            "sine": 0,
            "cosine": 1,
            "tangent": 0,
            "cotangent": None,
            "secant": 1,
            "cosecant": None,
        }
    if principal_interval_angle == PI_OVER_TWO:
        return {
            "angle": angle,
            "principal_interval": principal_interval_angle,
            "quadrant": QuadrantLocation.YPositive,
            "sine": 1,
            "cosine": 0,
            "tangent": None,
            "cotangent": 0,
            "secant": None,
            "cosecant": 1,
        }
    if principal_interval_angle == math.pi:
        return {
            "angle": angle,
            "principal_interval": principal_interval_angle,
            "quadrant": QuadrantLocation.XNegative,
            "sine": 0,
            "cosine": -1,
            "tangent": 0,
            "cotangent": None,
            "secant": -1,
            "cosecant": None,
        }
    if principal_interval_angle == THREE_PI_OVER_TWO:
        return {
            "angle": angle,
            "principal_interval": principal_interval_angle,
            "quadrant": QuadrantLocation.YNegative,
            "sine": -1,
            "cosine": 0,
            "tangent": None,
            "cotangent": 0,
            "secant": None,
            "cosecant": -1,
        }

    sine = math.sin(principal_interval_angle)
    cosine = math.cos(principal_interval_angle)
    tangent = math.tan(principal_interval_angle)
    cotangent = tan_cot(tangent)
    secant = cos_sec(cosine)
    cosecant = sin_csc(sine)

    return {
        "angle": angle,
        "principal_interval": principal_interval_angle,
        "quadrant": quadrant_location,
        "sine": sine,
        "cosine": cosine,
        "tangent": tangent,
        "cotangent": cotangent,
        "secant": secant,
        "cosecant": cosecant,
    }

def values_from_sine(value):
    angle = math.asin(value)
    return values_from(angle)

def values_from_cosine(value):
    angle = math.acos(value)
    return values_from(angle)

def values_from_tangent(value):
    angle = math.atan(value)
    return values_from(angle)

def values_from_cotangent(value):
    tangent = tan_cot(value)
    angle = math.atan(tangent)
    return values_from(angle)

def values_from_cosecant(value):
    sine = sin_csc(value)
    angle = math.asin(sine)
    return values_from(angle)

def values_from_secant(value):
    cosine = cos_sec(value)
    angle = math.acos(cosine)
    return values_from(angle)

