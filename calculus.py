#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt

def f(coeff1=1, coeff2=1, coeff3=1, coeff4=1):
  def fn(x):
    return coeff1 * x ** 3 + coeff2 * x ** 2 + coeff3 * x + coeff4
  return fn

order = 3
max_x = 20


def main(args=None):
    coefs = np.random.randn(order + 1) 

    x = np.linspace(-max_x, max_x, 101)
    y = np.zeros(len(x))

    fname = '$y = '
    for i, c in enumerate(coefs):
        y += c * x ** i
        fname += '+ '[int(c < 0 or i == 0)] + f'{c:.2f}x^{i}'

    plt.title(fname + '$')
    plt.plot(x, y, color='blue')
    plt.show()


if __name__ == "__main__":
    main()
