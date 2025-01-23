#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = []
    for i in matrix:
        y = []
        for j in i:
            p = (j * j)
            y.append(p)
        x.append(y)
    return x
