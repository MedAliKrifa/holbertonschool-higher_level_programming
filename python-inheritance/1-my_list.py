#!/usr/bin/python3
"""inheritance"""


class MyList(list):
    """def class"""
    def __init__(self):
        """initilization"""
        list.__init__(self)
    def print_sorted(self):
        """def self"""
        print(sorted(self))
