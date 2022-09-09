#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) in range(96, 123):
            upper = chr(ord(x) - 32)
        else:
            upper = x
        print("{}".format(upper), end='')
    print()
