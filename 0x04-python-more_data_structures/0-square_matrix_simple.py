#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) is None:
        return None

    square = []
    for i in range(len(matrix)):
        if len(matrix[i]) == 0 or matrix[i] is None:
            square.append([])
            continue
        squares = [matrix[i][s]**2 for s in range(len(matrix[i]))]
        square.append(squares)
    return square
