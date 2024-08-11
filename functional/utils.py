import os
import sys
from maths.arithmetic.utils import asub

sys.path.extend([os.getcwd()])


def do_for(f):
    def fn(a):
        return list(map(f, a))
    return fn
