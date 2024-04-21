#!/usr/bin/python3
""" load_from_json_file function """
json = __import__('json')


def load_from_json_file(filename):
    """ function creates an Object from a “JSON file”

        Args:
            filename(str): string containing name of json file

    """
    with open(filename, "r") as lfile:
        content = lfile.read()
        loaded = json.loads(content)

    return loaded
