#!/usr/bin/python3
def uppercase(str):
    s = {}
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            c = (ord(i) - 32)
            print('{}'.format(chr(c)), end='')
        else:
            print('{}'.format(i), end='')
    print()
