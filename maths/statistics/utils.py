import os
import sys
from maths.arithmetic.utils import asub

sys.path.extend([os.getcwd()])


def mean(a):
    return sum(a) / len(a)


def minus_mean(a):
    f = asub(mean(a))
    return list(map(f, a))


def variance(vs):  # Suggested by Copilot
    m = mean(vs)
    return sum(asub(m)(v) ** 2 for v in vs) / len(vs)


def standard_deviation(vs):  # Suggested by Copilot
    return variance(vs) ** 0.5
