#!/usr/bin/python3
""" function that divides the matrix provided
"""


def matrix_divided(matrix, div):
    """ function divides the elements
        of matriox by div
        Args:
            matrix(list): multidimentional list
            div(int): number to divide each element

        Return:
            list: a multidimentional array

        Exceptions:
            TypeError: if not equal element on each array
            ZeroDivisionError: div is 0
    """ 
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if isinstance(matrix, list):
        if not all(isinstance(item, list) for item in matrix):
            raiseMatrixTypeError()
    elif matrix is None or not isinstance(matrix, list):
        raiseMatrixTypeError()
    if div == 0:
        raise ZeroDivisionError("division by zero")
    try:
        d = int(div)
    except (ValueError, TypeError):
        raise TypeError("div must be a number")

    init_len = len(matrix[0])
    for i in range(len(matrix)):
        row = []
        if init_len != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(item, (int, float)) for item in matrix[i]):
            raiseMatrixTypeError()
        for j in range(init_len):
            row.append(float("{:.2}".format(matrix[i][j] / div)))
        new_matrix.append(row)
    return new_matrix

def raiseMatrixTypeError():
    """The function raises a type Error for
       Errors with matrix collected in matrx_divided
    """
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

