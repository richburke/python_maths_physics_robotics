import os
import sys
import math
import matplotlib.pyplot as plt

sys.path.extend([os.getcwd()])

'''
def plot_polar(fn, start, end, step):
    x = [i for i in range(start, end, step)]
    y = [fn(i) for i in x]
    plt.polar(x, y)
    plt.show()
'''

def y_sine(x, a, b, x_shift = 0, y_shift = 0):
    return a * math.sin(b * (x - x_shift)) + y_shift

def y_cosine(x, a, b, x_shift = 0, y_shift = 0):
    return a * math.cos(b * (x - x_shift)) + y_shift

def y_tangent(x, a, b, x_shift = 0, y_shift = 0):
    return a * math.tan(b * (x - x_shift)) + y_shift

def y_cosecant(x, a, b, x_shift = 0, y_shift = 0):
    return a * (1 / math.sin(b * (x - x_shift))) + y_shift

def y_secant(x, a, b, x_shift = 0, y_shift = 0):
    return a * (1 / math.cos(b * (x - x_shift))) + y_shift

def y_cotangent(x, a, b, x_shift = 0, y_shift = 0):
    return a * (1 / math.tan(b * (x - x_shift))) + y_shift

def plot_sine_wave(x = [-math.pi / 2, -math.pi/ 4, 0, math.pi / 4, math.pi / 2], a = 1, b = 1, x_shift = 0, y_shift = 0):
    y = [y_sine(i, a, b, x_shift, y_shift) for i in x]
    plt.plot(x, y)
    plt.show()