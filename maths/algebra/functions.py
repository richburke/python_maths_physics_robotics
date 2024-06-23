import os
import sys

sys.path.extend([os.getcwd()])

# Expects a unary function.
def is_function_even(fn):
    return True if fn(1) == fn(-1) else False

# Expects a unary function.
def is_function_odd(fn):
    return not is_function_even(fn)