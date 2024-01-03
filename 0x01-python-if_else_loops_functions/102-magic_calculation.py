#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c

# Uncomment the following lines and run ./filename to see byte code
# import dis
# print(dis.dis(magic_calculation))
