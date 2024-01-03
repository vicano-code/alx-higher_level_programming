#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char is not (ord('q')) and char is not (ord('e')):
        print('{}'.format(chr(char)), end='')
