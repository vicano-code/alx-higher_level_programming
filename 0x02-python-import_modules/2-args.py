#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv) - 1
    s = ""
    if (num_args == 0):
        s = "arguments."
    elif (num_args == 1):
        s = "argument:"
    else:
        s = "arguments:"
    print("{:d} {:s}".format(num_args, s))
    for i in range(1, num_args + 1):
        print("{:d}: {:s}".format(i, argv[i]))
