import os
import sys
from maths.arithmetic.utils import asquared_sum, asubtract
from maths.statistics.defines import Mean

sys.path.extend([os.getcwd()])


def mean(type=Mean.QUADRATIC):
    def fn(a):
        return arithmetic_mean(a) if type == Mean.ARITHMETIC else quadratic_mean(a)
    return fn


def arithmetic_mean(a):
    return sum(a) / len(a)


def quadratic_mean(a):
    return asquared_sum(a) / len(a) ** 0.5


def minus_mean(type=Mean.QUADRATIC):
    def fn(a):
        f = asubtract(mean(type)(a))
        return list(map(f, a))
    return fn


def variance(sample=True):
    def fn(a):
        return sample_variance(a) if sample else population_variance(a)
    return fn


def sample_variance(a):
    return asquared_sum(minus_mean(a)) / (len(a) - 1)


def population_variance(a):
    return asquared_sum(minus_mean(a)) / len(a)


def standard_deviation(sample=True):
    def fn(a):
        return variance(sample)(a) ** 0.5
    return fn
