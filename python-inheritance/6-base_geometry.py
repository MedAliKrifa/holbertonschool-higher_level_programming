#!/usr/bin/python3
"""inheritance"""


from logging import exception


class BaseGeometry:
    """empty class"""
    def area(self):
        """def area"""
        raise Exception ("area() is not implemented")
