#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if list is None:
        raise TypeError("list must be a list of integers")

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if not isinstance(list[i], (int, float)):
            raise TypeError("All values should be an integer or float")
        if list[i] > result:
            result = list[i]
        i += 1
    return result
