#!/usr/bin/python3
""" pascal_triangle """


def pascal_triangle(n):
    """ Function returns a list of lists of integers
        representing the Pascal’s triangle of n

        Args:
            n(int): number to represent in pascal triangle

        Return:
            a list of integers at a specific part
            of pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle

    ref = []
    for i in range(1, (n + 1)):
        part = []
        for j in range(i):
            if len(part) == 0 or j == (i - 1):
                part.append(1)
            else:
                part.append((ref[j - 1] + ref[j]))

        triangle.append(part)
        ref = part[:]
    return triangle
