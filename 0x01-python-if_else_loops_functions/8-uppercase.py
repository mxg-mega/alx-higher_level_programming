#!/usr/bin/python3
def uppercase(str):
    s = ''
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = (ord(str[i]) - 32)
            s += '{}'.format(chr(c))
        else:
            s += '{}'.format(str[i])
    print(s)
