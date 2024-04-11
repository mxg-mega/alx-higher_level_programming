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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
