#!/usr/bin/python3
""" functions that indents texts """


def text_indentation(text):
    """ function prints text indented with two line if
        it encounters . ? or :
        Args:
            text(str): text to indent
    """
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")

    indent_marks = ['.', '?', ':']
    string = ''

    for i in range(len(text)):
        if text[i] in indent_marks:
            string += text[i] + "\n\n"
            line = string
            while line[0] == ' ':
                line = line[1:]
            print(line, end='')
            string = ''
        else:
            string += text[i]
    while string[0] == ' ':
        string = string[1:]
    print(string, end='')
