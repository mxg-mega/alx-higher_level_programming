#!/usr/bin/python3
""" function that divides the matrix provided
"""


def matrix_divided(matrix, div):
    """Divides each element of a matrix by div.

    Args:
        matrix (list): A matrix (list of lists) of integers or floats.
        div (int or float): The number to divide each element by.

    Returns:
        list: A new matrix with elements divided by div, rounded to two decimal places.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats,
                   if div is not a number, or if matrix contains non-numeric elements.
        ZeroDivisionError: If div is 0.
        TypeError: If each row of the matrix does not have the same size.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("matrix must contain only integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrix
