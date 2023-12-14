#!/usr/bin/python3
for i in range(26):
    letter = ord('z')
    if letter <= ord('z') and letter >= ord('a'):
        if (i % 2) == 0:
            letter -= i
        else:
            letter -= i
            letter -= 32

        print("{}".format(chr(letter)), end='')
