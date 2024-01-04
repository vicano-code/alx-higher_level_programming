#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        print("{} {} {} = {}".format(a, op, b, operator[op](a, b)))
