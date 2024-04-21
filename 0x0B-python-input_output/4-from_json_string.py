#!/usr/bin/python3
""" from_json_strin funtion """
json = __import__('json')


def from_json_string(my_str):
    """ function returns an object (Python data structure)
        represented by a JSON string

        Args:
            my_str: the string to deserialize
        Return:
              dse: deserialized string
    """
    dse = json.loads(my_str)
    return dse
