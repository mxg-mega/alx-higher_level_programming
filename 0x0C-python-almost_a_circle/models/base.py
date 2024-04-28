#!/usr/bin/python3
""" Base Class """
import json
import csv


class Base:
    """ Base class
        Attributes:
            nb_objects: private class atrributes rep
            Nyumber of objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__ instantiates the class

            Args:
                id(int): id of an object,
                initialized to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ The static method to_json_string
            that returns the JSON string representation
            of list_dictionaries.

            Args:
                list_dictionaries(list): the data to
                                         convert to json format
        """
        if list_dictionaries is None:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @staticmethod
    def from_json_string(json_string):
        """ The static method from_json_string
            that returns the list of the JSON string
            representation json_string

            Args:
                json_string: string to load from json format

            Returns:
                converted json string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ The class method create
            that returns an instance with all attributes
            already set

            Args:
                dictionary(dict): a double pointer to a dictionary
            Returns:
                New created instance
        """
        cls_dummy = cls()
        cls_dummy.update(**dictionary)
        return cls_dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """ The class method save_to_file that writes
            the JSON string representation of list_objs to a file

            Args:
                cls: class of objects
                list_objs: is a list of instances who inherits
                           of base.
        """
        objs = []
        if list_objs is None or list_objs == objs:
            objs = []
        else:
            for i in list_objs:
                objs.append(i.to_dictionary())

        with open("{}.json".format(cls.__name__), "w") as sf:
            sf.write(cls.to_json_string(objs))

    @classmethod
    def load_from_file(cls):
        """ The class method load_from_file eturns a list of instances

            Args:
                cls: the class to return its instances

            Returns:
                list loaded from a file
        """
        objs = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as lfile:
                content = lfile.read()
                loaded = cls.from_json_string(content)
        except Exception as e:
            return objs
        for i in range(len(loaded)):
            objs.append(cls.create(**loaded[i]))
        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ The class method save_to_file_csv that writes
            the CSV string representation of list_objs to a file

            Args:
                cls: class of objects
                list_objs: is a list of instances who inherits
                           of base.
        """
        if list_objs is None:
            objs = []
        else:
            objs = []
            for i in list_objs:
                objs.append(i.to_csv_format())

        with open("{}.csv".format(cls.__name__), "w") as sf:
            csv_writer = csv.writer(sf)
            for i in objs:
                csv_writer.writerow(i)

    @classmethod
    def load_from_file_csv(cls):
        """ The class method load_from_file_csv
            returns a list of instances

            Args:
                cls: the class to return its instances

            Returns:
                list loaded from a file
        """
        objs = []
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline='', encoding="utf-8") as csvfile:
                csv_reader = csv.reader(csvfile)
                for line in csv_reader:
                    try:
                        row = [int(value) for value in line]
                        dummy = cls()
                        dummy.update(*row)
                        objs.append(dummy)
                    except Exception as e:
                        print(e)
            return objs
        except Exception as e:
            objs = []
            return objs
