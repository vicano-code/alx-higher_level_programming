#!/usr/bin/python3
import sys

r = 0
num_args = len(sys.argv)
for i in range(1, num_args):
    r += int(sys.argv[i])
print(f"{r}\n")
