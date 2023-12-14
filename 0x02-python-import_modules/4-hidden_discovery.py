#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    dir_func = dir(hidden_4)
    for i in dir_func:
        if i[0] == '_' and i[1] == '_':
            continue
        else:
            print(i)
