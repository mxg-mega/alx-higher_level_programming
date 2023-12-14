#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    argc = len(sys.argv)
    argv = sys.argv
    if argc != 4:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator == '+':
            print('{} {} {} = {}'.format(a, operator, b, add(a, b)))
        elif operator == '-':
            print('{} {} {} = {}'.format(a, operator, b, sub(a, b)))
        elif operator == '*':
            print('{} {} {} = {}'.format(a, operator, b, mul(a, b)))
        elif operator == '/':
            print('{} {} {} = {}'.format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /", file=sys.stderr)
            sys.exit(1)
