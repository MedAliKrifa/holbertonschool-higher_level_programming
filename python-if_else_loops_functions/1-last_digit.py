#!/usr/bin/python3
from contextlib import nullcontext
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    n = number % 10
    if n == 0:
        print(f"Last digit of {number * -1} is {n} and is 0")
    else:
        print(
            f"Last digit of {number*-1} is {n*-1} and is less than 6 and not 0"
            )
else:
    n = number % 10
    if n > 5:
        print(f"Last digit of {number} is {n} and is greater than 5")
    elif n > 0 and n < 6:
        print(f"Last digit of {number} is {n} and is less than 6 and not 0")
    elif n == 0:
        print(f"Last digit of {number * -1} is {n} and is 0")
