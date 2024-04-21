#!/usr/bin/python3
""" Class_to_json Function"""


def class_to_json(obj):
    """ function that returns the dictionary description
        with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

        Args:
            obj: instance of a class

        Return:
            a dictionary representation
    """
    attributeDict = obj.__dict__
    return attributeDict
