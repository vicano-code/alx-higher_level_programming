#!/usr/bin/python3
'''
a function that returns a tuple with the length 
of a string and its first character.
'''
def multiple_returns(sentence):
    size = len(sentence)
    if size == 0:
        first_char = None
    first_char = sentence[0]
    return (size, first_char)
