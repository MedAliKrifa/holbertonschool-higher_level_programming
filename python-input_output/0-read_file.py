#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """function to read file using with"""
    with open(filename, mode='r', encoding='utf-8') as f:
        read_file = f.read()
        print(read_file, end="")
