#!/usr/bin/python3
""" Student Class """


class Student:
    """ Student Class
        Attributes:
            first_name(public, str): first name of student
            last_name(public, str): last name of student
            age(public, int): age of student
    """

    """ Init istantiates the class
        Args:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ function retreives a dictionary representation
            of class instance
        """
        return self.__dict__
