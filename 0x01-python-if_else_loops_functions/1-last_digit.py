#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of"
if number < 0:
    last_digit = -(abs(number) % 10)
elif number == 0:
    last_digit = 0
else:
    last_digit = number % 10
if last_digit > 5:
    print(f"{s} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{s} {number} is {last_digit} and is 0")
else:
    print(f"{s} {number} is {last_digit} and is less than 6 and not 0")
