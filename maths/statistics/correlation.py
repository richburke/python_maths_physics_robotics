import os
import sys
from operator import itemgetter
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from functional.utils import do_for
from maths.arithmetic.utils import asquared_sum
from maths.statistics.defines import Mean
from maths.statistics.utils import mean, minus_mean

sys.path.extend([os.getcwd()])


def mean_squared_error(y_actual, y_predicated):
    return sum((y_actual[i] - y_predicated[i]) ** 2 for i in range(len(y_actual))) / len(y_actual)


def difference_mean_squared_sum(a):
    return asquared_sum(minus_mean(a))


def least_squares_regression(xs):
    def fn(ys):
        x_mean = mean(Mean.QUADRATIC)(xs)
        y_mean = mean(Mean.QUADRATIC)(ys)
        x_minus_mean = minus_mean(Mean.QUADRATIC)(xs)
        y_minus_mean = minus_mean(Mean.QUADRATIC)(ys)
        x_minus_mean_squared_sum = asquared_sum(x_minus_mean)

        product = [x * y for x, y in zip(x_minus_mean, y_minus_mean)]
        product_sum = sum(product)

        slope = product_sum / x_minus_mean_squared_sum
        y_intercept = y_mean - slope * x_mean

        return lambda x: slope * x + y_intercept
    return fn


def linear_regression_model(xs):
    def fn(ys):
        x = xs.reshape(-1, 1)
        y = ys.reshape(-1, 1)
        return LinearRegression().fit(x, y)
    return fn


def linear_regression(xs):
    def fn(ys):
        model = linear_regression_model(xs)(ys)

        def gn(x_predicated):
            x_predicated = x_predicated.reshape(-1, 1)
            return model.predict(x_predicated)
        return gn
    return fn


def polynomial_regression_model(degree=2):
    def fn(xs):
        def gn(ys):
            x = xs.reshape(-1, 1)
            y = ys.reshape(-1, 1)
            poly_features = PolynomialFeatures(
                degree=degree, include_bias=False)
            x_poly = poly_features.fit_transform(x)
            return {"features": poly_features,
                    "model": LinearRegression().fit(x_poly, y)}
        return gn
    return fn


def polynomial_regression(degree=2):
    def fn(xs):
        def gn(ys):
            features, model = itemgetter('features', 'model')(
                polynomial_regression_model(degree)(xs)(ys))

            def hn(x_predicated):
                x_predicated = x_predicated.reshape(-1, 1)
                x_predicated_poly = features.fit_transform(x_predicated)
                return model.predict(x_predicated_poly)
            return hn
        return gn
    return fn

# AKA r


def pearson_correlation_coefficient(xs):
    def fn(ys):
        x_minus_mean = minus_mean(Mean.QUADRATIC)(xs)
        y_minus_mean = minus_mean(Mean.QUADRATIC)(ys)
        x_minus_mean_squared_sum = asquared_sum(x_minus_mean)
        y_minus_mean_squared_sum = asquared_sum(y_minus_mean)

        numerator = sum([x * y for x, y in zip(x_minus_mean, y_minus_mean)])
        denominator = (x_minus_mean_squared_sum *
                       y_minus_mean_squared_sum) ** 0.5
        return numerator / denominator
    return fn


# How much of the change in y can be explained by the change in x?


def r_squared(xs):
    def fn(ys):
        f = least_squares_regression(xs)(ys)
        y_estimated = do_for(f)(xs)
        y_minus_mean = minus_mean(Mean.QUADRATIC)(ys)
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
