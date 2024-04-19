#!/usr/bin/python3
""" This Module has a function that checks
    for the instances of a class """


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False.

        Args:
            obj: the object
            a_class: the class name
        return:
            True(bool): if it is a subclass or type of subclass
            False(bool): obj has no relation to a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
