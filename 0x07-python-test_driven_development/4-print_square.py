#!/usr/bin/python3
""" Funtions to print a square
"""


def print_square(size):
    """ function prints a square using #
        of size size

        Args:
            size(int, float): size of square
    """
    if not isinstance(size,
                      (int, float)) or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    try:
        s = int(size)
    except (ValueError, TypeError):
        raise TypeError("size must be an integer")

    for i in range(s):
        for j in range(s):
            print("#", end='')
        print()
