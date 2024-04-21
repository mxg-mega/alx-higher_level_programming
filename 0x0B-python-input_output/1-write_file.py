#!/usr/bin/python3
""" write_file function"""


def write_file(filename='', text=''):
    """ function opens a file and writes the text to it

        Args:
            filename(str): name of the file
            text(str): the text to write
        returns:
            nb_chars: number of characters written
    """
    with open(filename, "w") as wf:
        nb_chars = wf.write(text)
    return nb_chars
