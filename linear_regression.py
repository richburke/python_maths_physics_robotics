#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
from maths.statistics.defines import Mean
from maths.statistics.utils import mean
from maths.statistics.correlation import linear_regression


def main(args=None):
    xs = np.array([1, 2, 3, 4, 5])
    ys = np.array([2, 4, 5, 4, 5])

    axis = plt.gca()
    axis.set_xlim([0, 6])
    axis.set_ylim([0, 6])
    plt.scatter(xs, ys)

    x_mean = mean(Mean.ARITHMETIC)(xs)
    y_mean = mean(Mean.ARITHMETIC)(ys)
    plt.plot([x_mean, x_mean], [0, 6], color='red', linestyle='dashed')
    plt.plot([0, 6], [y_mean, y_mean], color='red', linestyle='dashed')

    xn = np.linspace(0, 6, 100)
    yn = linear_regression(xs)(ys)(xn)
    plt.plot(xn, yn, color='blue', linestyle='dashed')
    plt.show()


if __name__ == "__main__":
    main()
