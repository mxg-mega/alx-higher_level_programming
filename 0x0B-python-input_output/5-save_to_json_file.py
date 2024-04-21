#!/usr/bin/python3
""" save_to_json_file function """
json = __import__("json")


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
        using a JSON representation

        Args:
            my_obj: object to serialize
            filename: name of file to save serialized obj
        Return:
    """
    with open(filename, "w") as jfile:
        serial = json.dumps(my_obj)
        jfile.write(serial)
