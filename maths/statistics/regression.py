import os
import sys
from functional.utils import do_for
from maths.arithmetic.utils import asquared_sum
from maths.statistics.utils import mean, minus_mean

sys.path.extend([os.getcwd()])


def mean_squared_error(y_actual, y_predicated):
    return sum((y_actual[i] - y_predicated[i]) ** 2 for i in range(len(y_actual))) / len(y_actual)


def difference_mean_squared_sum(a):
    return asquared_sum(minus_mean(a))


def least_squares_regression(xs):
    def fn(ys):
        x_mean = mean(xs)
        y_mean = mean(ys)
        x_minus_mean = minus_mean(xs)
        y_minus_mean = minus_mean(ys)
        x_minus_mean_squared_sum = asquared_sum(x_minus_mean)

        product = [x * y for x, y in zip(x_minus_mean, y_minus_mean)]
        product_sum = sum(product)

        slope = product_sum / x_minus_mean_squared_sum
        y_intercept = y_mean - slope * x_mean

        return lambda x: slope * x + y_intercept
    return fn

# How much of the change in y can be explained by the change in x?


def r_squared(xs):
    def fn(ys):
        f = least_squares_regression(xs)(ys)
        y_estimated = do_for(f)(xs)
        y_minus_mean = minus_mean(ys)
        y_minus_y_estimated = list(
            map(lambda y, y_hat: y - y_hat, ys, y_estimated))

        return 1 - asquared_sum(y_minus_y_estimated) / asquared_sum(y_minus_mean)
    return fn


def standard_error_of_the_estimate(xs):
    def fn(ys):
        n = len(xs)
        f = least_squares_regression(xs)(ys)
        y_estimated = do_for(f)(xs)
        y_minus_y_estimated = list(
            map(lambda y, y_hat: y_hat - y, ys, y_estimated))

        return (asquared_sum(y_minus_y_estimated) / (n - 2)) ** 0.5
    return fn
