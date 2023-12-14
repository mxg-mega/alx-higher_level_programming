#!/usr/bin/python3
for i in range(26):
    l = ord('z')
    if l <= ord('z') and l >= ord('a'):
        if (i % 2) == 0:
            l -= i
        else:
            l -= i
            l -= 32

        print("{}".format(chr(l)), end='')
    
