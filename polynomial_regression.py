#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
from maths.statistics.correlation import polynomial_regression

def main(args=None):
    xp = 4 * np.random.rand(100, 1) - 2
    yp = 4 + 2 * xp + 5 * xp ** 2 + 10 * np.random.randn(100, 1)

    x_vals = np.linspace(-2, 2, 100)
    y_vals = polynomial_regression(2)(xp)(yp)(x_vals)

    plt.scatter(xp, yp)
    plt.plot(x_vals, y_vals, color='gray', linestyle='dashed')
    plt.show()


if __name__ == "__main__":
    main()
