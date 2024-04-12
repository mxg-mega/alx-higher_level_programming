#!/usr/bin/python3
""" The functions here says the name inputed
    every function will be tested in the tests directory
"""


def say_my_name(first_name, last_name=""):
    """ function prints out
    'My name <first_name> <last_name>>'

    Args:
        first_name(string): first string
        last_name(string): second string
    Return:
        no Return
    Exceptions:
        TypeError: all names must be string
    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
