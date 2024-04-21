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

    def to_json(self, attrs=None):
        """ function retreives a dictionary representation
            of class instance
            Args:
                attrs: list of attributes to get
        """
        if attrs is None:
            return self.__dict__
        else:
            attrsLookup = {}
            for i in attrs:
                try:
                    attrsLookup[i] = self.__dict__[i]
                except Exception:
                    continue
        return attrsLookup

    def reload_from_json(self, json):
        """ function that replaces all attributes of the Student instance
            Args:
                json: data to reload to json
        """
        for i in json:
            self.__dict__[i] = json[i]
