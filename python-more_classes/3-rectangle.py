#!/usr/bin/python3
"""class square to define a rectangle"""


class Rectangle:
    """class square to define a Rectangle"""
    pass

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        print_rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                print_rectangle += "#"
            if i != (self.__height - 1):
                print_rectangle += ("\n")
        return (print_rectangle)
