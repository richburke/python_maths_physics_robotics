import os
import sys

sys.path.extend([os.getcwd()])

def scale_vector(scalar):
    def fn(vector):
        return [scalar * component for component in vector]
    return fn

def add_vector(vector1):
    def fn(vector2):
        return [vector1[i] + vector2[i] for i in range(len(vector1))]
    return fn

def subtract_vector(vector1):
    def fn(vector2):
        return [vector1[i] - vector2[i] for i in range(len(vector1))]
    return fn

def dot_product(vector1):
    def fn(vector2):
        return sum([vector1[i] * vector2[i] for i in range(len(vector1))])
    return fn

def cross_product(vector1):
    def fn(vector2):
        return [
            vector1[1] * vector2[2] - vector1[2] * vector2[1],
            vector1[2] * vector2[0] - vector1[0] * vector2[2],
            vector1[0] * vector2[1] - vector1[1] * vector2[0]
        ]
    return fn

def magnitude(vector):
    return sum([component ** 2 for component in vector]) ** 0.5