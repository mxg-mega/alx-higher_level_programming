#!/usr/bin/python3
"""In this module we write an addition
   function and writing a doctest
"""


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
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")
    try:
        result = int(a) + int(b)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")

    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
