#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    ldigit = number % 10
    if ldigit == 0:
        print(f"Last digit of {number * -1} is {ldigit} and is 0")
    else:
        print(f"Last digit of {number * -1} is {ldigit * -1} and is less than 6 and not 0")
else:
    ldigit = number % 10
    if ldigit > 5:
        print(f"Last digit of {number} is {ldigit} and is greater than 5")
    elif ldigit == 0:
        print(f"Last digit of {number} is {ldigit} and is 0")
    else:
        print(f"Last digit of {number} is {ldigit} and is less than 6 and not 0")
