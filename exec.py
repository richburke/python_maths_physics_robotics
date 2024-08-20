#!/usr/bin/env python3
import numpy as np
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt
from maths.arithmetic.utils import asubtract, asquared_sum
from maths.statistics.defines import Mean
from maths.statistics.utils import mean
from maths.statistics.correlation import linear_regression, polynomial_regression_model, polynomial_regression, least_squares_regression, r_squared, standard_error_of_the_estimate


def main(args=None):
    # xs = np.linspace(468, 132, 100)
    # ys = np.linspace(0, 8, 100)
    xs = np.array([468, 342, 251, 185, 132])
    ys = np.array([0, 2, 4, 6, 8])

    max_x = 500
    max_y = 9

    axis = plt.gca()
    axis.set_xlim([0, max_x])
    axis.set_ylim([0, max_y])
    plt.scatter(xs, ys)

    x_mean = mean(Mean.ARITHMETIC)(xs)
    y_mean = mean(Mean.ARITHMETIC)(ys)
    plt.plot([x_mean, x_mean], [0, max_x], color='red', linestyle='dashed')
    plt.plot([0, max_y], [y_mean, y_mean], color='red', linestyle='dashed')

    xn = np.linspace(0, max_x, len(xs))
    yn = linear_regression(xs)(ys)(xn)
    plt.plot(xn, yn, color='blue', linestyle='dashed')
    # plt.show()

    # xp = 4 * np.random.rand(100, 1) - 2
    # yp = 4 + 2 * xp + 5 * xp ** 2 + 10 * np.random.randn(100, 1)

    # x_vals = np.linspace(-2, 2, 100)
    # y_vals = polynomial_regression(2)(xp)(yp)(x_vals)

    # plt.scatter(xp, yp)
    # plt.plot(x_vals, y_vals, color='gray', linestyle='dashed')
    # plt.show()

    # print(r_squared(xs)(xn))
    # print(r_squared(ys)(yn))

    # print(ys)
    # print(yn)

    y_true = ys.reshape(-1, 1)
    y_predicated = yn
    # y_predicated = yn.flatten()
    y_predicated = y_predicated[::-1]
    # y_true = [0, 2, 4, 6, 8]
    # y_predicated = [10.448, 7.524, 4.6, 1.676, -1.248]
    print(r2_score(xs.reshape(-1, 1), ys.reshape(-1, 1)))
    # print(r_squared(y_true)(y_predicated))
    # print(r2_score(ys.reshape(-1, 1), yn))
    # print(standard_error_of_the_estimate(xs)(ys))


if __name__ == "__main__":
    main()
