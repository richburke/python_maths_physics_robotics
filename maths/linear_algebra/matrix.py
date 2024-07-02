import os
import sys

sys.path.extend([os.getcwd()])

def identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def scale_matrix(scalar):
    def fn(matrix):
        return [[scalar * component for component in row] for row in matrix]
    return fn

def add_matrix(matrix1):
    def fn(matrix2):
        return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return fn

def subtract_matrix(matrix1):
    def fn(matrix2):
        return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return fn

def multiply_matrix(matrix1):
    def fn(matrix2):
        return [[sum([matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))]) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    return fn

