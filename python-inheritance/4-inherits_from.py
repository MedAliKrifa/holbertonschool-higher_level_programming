#!/usr/bin/python3
"""inheritance"""


def inherits_from(obj, a_class):
    """compare obj and a class"""
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
