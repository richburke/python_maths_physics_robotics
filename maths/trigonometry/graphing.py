import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from maths.trigonometry.defines import PI, TWO_PI, TrigFunction
from maths.trigonometry.identities import sin_csc

sys.path.extend([os.getcwd()])

RANGE_PRINCIPAL_INTERVAL = np.linspace(0, TWO_PI, 360)

'''
@todo
If I get the time I'd like to improve these graphs. The first place to start
would be labeling the X-axis. It would be nice to see those in radians.
https://mikequentelsoftware.blogspot.com/2012/10/example-of-trigonometric-functions-in.html
'''

'''
def plot_polar(fn, start, end, step):
    x = [i for i in range(start, end, step)]
    y = [fn(i) for i in x]
    plt.polar(x, y)
    plt.show()
'''

def y_sine(x, vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
    return vertical_scalar * math.sin(horizontal_scalar * (x - x_shift)) + y_shift

def y_cosine(x, vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
    return vertical_scalar * math.cos(horizontal_scalar * (x - x_shift)) + y_shift

def y_tangent(x, vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
    return vertical_scalar * math.tan(horizontal_scalar * (x - x_shift)) + y_shift

def y_cosecant(x, vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
    csc = sin_csc( math.sin(horizontal_scalar * (x - x_shift)))
    return vertical_scalar * csc + y_shift

def y_secant(x, vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
    return vertical_scalar * (1 / math.cos(horizontal_scalar * (x - x_shift))) + y_shift

def y_cotangent(x, vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
    return vertical_scalar * (1 / math.tan(horizontal_scalar * (x - x_shift))) + y_shift

def amplitude_from_scalar(vertical_scalar = 1):
    np.abs(vertical_scalar)

def amplitude(minmax):
    min, max = minmax
    np.abs((max - min) / 2)

def period(trig_function = TrigFunction.SINE):
    def fn(horizontal_scalar = 1):
        if trig_function == TrigFunction.SINE or \
           trig_function == TrigFunction.COSINE or \
           trig_function == TrigFunction.SECANT or \
           trig_function == TrigFunction.COSECANT:
            return TWO_PI / np.abs(horizontal_scalar)
        return PI / np.abs(horizontal_scalar)
    return fn

def plot_sine(theta = RANGE_PRINCIPAL_INTERVAL):
    def fn(vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
        y = [y_sine(i, vertical_scalar, horizontal_scalar, x_shift, y_shift) for i in theta]
        plt.plot(theta, y)
        plt.show()
    return fn

def plot_sine_with_unscaled(theta = RANGE_PRINCIPAL_INTERVAL):
    def fn(vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
        y1 = [y_sine(i) for i in theta]
        y2 = [y_sine(i, vertical_scalar, horizontal_scalar, x_shift, y_shift) for i in theta]
        plt.plot(theta, y1, 'k--')
        plt.plot(theta, y2, 'b')
        plt.show()
    return fn

def plot_cosine(theta = RANGE_PRINCIPAL_INTERVAL):
    def fn(vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
        y = [y_cosine(i, vertical_scalar, horizontal_scalar, x_shift, y_shift) for i in theta]
        plt.plot(theta, y)
        plt.show()
    return fn

def plot_cosine_with_unscaled(theta = RANGE_PRINCIPAL_INTERVAL, vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
    def fn(vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0):
        y1 = [y_cosine(i) for i in theta]
        y2 = [y_cosine(i, vertical_scalar, horizontal_scalar, x_shift, y_shift) for i in theta]
        plt.plot(theta, y1, 'k--')
        plt.plot(theta, y2, 'b')
        plt.show()
    return fn

def plot_cosecant(theta = RANGE_PRINCIPAL_INTERVAL):
    def fn(vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0, y_axis_min=-4, y_axis_max=4):
        y = [y_cosecant(i, vertical_scalar, horizontal_scalar, x_shift, y_shift) for i in theta]
        
        plt.xlim(theta.min() * 1.1, theta.max() * 1.1)
        plt.ylim(y_axis_min, y_axis_max)

        plt.plot(theta, y)
        plt.show()
    return fn

def plot_cosecant_with_unscaled(theta = RANGE_PRINCIPAL_INTERVAL):
    def fn(vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0, y_axis_min=-4, y_axis_max=4):
        y1 = [y_sine(i) for i in theta]
        y2 = np.array([y_cosecant(i, vertical_scalar, horizontal_scalar, x_shift, y_shift) for i in theta])

        plt.xlim(theta.min() * 1.1, theta.max() * 1.1)
        plt.ylim(y_axis_min, y_axis_max)
        
        plt.plot(theta, y1, 'k--')
        plt.plot(theta, y2, 'b')
        plt.show()
    return fn

def plot_secant(theta = RANGE_PRINCIPAL_INTERVAL):
    def fn(vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0, y_axis_min=-4, y_axis_max=4):
        y = [y_secant(i, vertical_scalar, horizontal_scalar, x_shift, y_shift) for i in theta]
        
        plt.xlim(theta.min() * 1.1, theta.max() * 1.1)
        plt.ylim(y_axis_min, y_axis_max)

        plt.plot(theta, y)
        plt.show()
    return fn

def plot_secant_with_unscaled(theta = RANGE_PRINCIPAL_INTERVAL):
    def fn(vertical_scalar = 1, horizontal_scalar = 1, x_shift = 0, y_shift = 0, y_axis_min=-4, y_axis_max=4):
        y1 = [y_cosine(i) for i in theta]
        y2 = np.array([y_secant(i, vertical_scalar, horizontal_scalar, x_shift, y_shift) for i in theta])

        plt.xlim(theta.min() * 1.1, theta.max() * 1.1)
        plt.ylim(y_axis_min, y_axis_max)
        
        plt.plot(theta, y1, 'k--')
        plt.plot(theta, y2, 'b')
        plt.show()
    return fn