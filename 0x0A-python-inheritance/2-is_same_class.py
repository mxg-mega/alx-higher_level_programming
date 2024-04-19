#!/usr/bin/python3
""" Function in ths module checks if an argument is
    an exact instance of a class """


def is_same_class(obj, a_class):
    """is_same_class function that returns True if the object
        is exactly an instance of the specified class ; otherwise False.
        Args:
            obj: any type of object/instance
            a_class: the class to compare if the obj is member
        return:
            True(bool): if obj is an instance of a_class
            False(bool): obj is not an instance of a_class
    """
    if type(obj) is a_class:
        return True
    return False
