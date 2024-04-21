#!/usr/bin/python3
""" append_write function """


def append_write(filename='', text=''):
    """ function appends text to the end of the file
        opened.

        Args:
            filename: name of file
            text: string containing the text to append

        Return:
            nb_chars(int): number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as af:
        nb_chars = af.write(text)
    return nb_chars
