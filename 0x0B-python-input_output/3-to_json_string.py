#!/usr/bin/python3
""" to_json_strin funtion """
json = __import__('json')


def to_json_string(obj):
    """ function returns the JSON representation of an object (string)

        Args:
            obj: the object to serialize
        Return:
            rep: representation of the object
    """
    rep = json.dumps(obj)
    return rep
