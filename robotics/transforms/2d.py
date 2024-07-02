import os
import sys
import math

sys.path.extend([os.getcwd()])

def translate_2d(x, y):
    def fn(point):
        return (point[0] + x, point[1] + y)
    return fn

def rotate_2d(angle):
    def fn(point):
        return (
            point[0] * math.cos(angle) - point[1] * math.sin(angle),
            point[0] * math.sin(angle) + point[1] * math.cos(angle)
        )
    return fn
