#!/usr/bin/python3
"""class square to define a square"""


class Square:
    """class square to define a square"""

    def __init__(self, size=0):
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
