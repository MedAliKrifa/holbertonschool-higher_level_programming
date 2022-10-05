#!/usr/bin/python3
"""Task 0"""


import json


def load_from_json_file(filename):
    """function to write file using with"""
    with open(filename, mode='r') as f:
        res = json.load(f)
        return res
