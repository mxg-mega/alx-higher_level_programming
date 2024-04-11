#!/usr/bin/python3

def add_integer(a, b=98):
    """ add_integer function
    returns the sum of two integers

    Args:
        a(int): first number
        b(int): second number
    Return:
        int(a + b): sum of the two ints
    Exceptions:
        TypeError: if either numbers is an integer
    """
    if (type(a) is not int):
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
