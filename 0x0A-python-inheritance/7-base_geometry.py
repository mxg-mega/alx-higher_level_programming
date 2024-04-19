#!/usr/bin/python3
""" BaseGeometry Class """


class BaseGeometry:
    """ Base Geometery class """

    """ function area is a non implemented function """
    def area(self):
        raise Exception("area() is not implemented")

    """ function validates the argument value
        Args:
            name: name of value to validate
            value: value to validate
        Raises:
            TypeError: name must be an integer
            ValueError: name must be greater than 0
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(str(name)))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(str(name)))
