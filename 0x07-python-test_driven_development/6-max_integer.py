#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None

    # If one number is negative, exchange it to a positive number
    copy_list = list[:]
    i = 0
    while i < len(copy_list):
        if copy_list[i] < 0:
            copy_list[i] *= -1
            break
        i += 1

    result = copy_list[0]
    i = 1
    while i < len(copy_list):
        if copy_list[i] > result:
            result = copy_list[i]
        i += 1
    return result
