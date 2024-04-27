#!/usr/bin/python3
""" Base Class """
import json


class Base:
    """ Base class
        Attributes:
            nb_objects: private class atrributes rep
            Nyumber of objects created.
    """
    __nb_objects = 0

    """ __init__ instantiates the class

        Args:
            id(int): id of an object,
            initialized to None.
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ The static method to_json_string
            that returns the JSON string representation
            of list_dictionaries.

            Args:
                list_dictionaries(list): the data to
                                         convert to json format
        """
        if type(list_dictionaries) is not list:
            raise TypeError("Data must be a list of dictionaries")
        if list_dictionaries == None:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string
