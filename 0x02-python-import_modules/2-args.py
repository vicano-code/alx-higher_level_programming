#!/usr/bin/python3
import sys
num_args = len(sys.argv) - 1
s = ""
if (num_args == 0):
    s = "arguments."
elif (num_args == 1):
    s = "argument:"
else:
    s = "arguments:"
print("{} {}".format(num_args, s))
for i in range(1, num_args + 1):
    print("{}: {}".format(i, sys.argv[i]))
