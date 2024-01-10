#!/usr/bin/python3

'''converts a Roman numeral to an integer'''


def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral = 0
    size = len(roman_string)
    for i in range(size):
        if i < (size - 1):
            if roman_string[i] not in roman_dict.keys():
                return 0
            if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
                roman_dict[roman_string[i]] = -(roman_dict[roman_string[i]])
        numeral += roman_dict[roman_string[i]]
    return numeral
