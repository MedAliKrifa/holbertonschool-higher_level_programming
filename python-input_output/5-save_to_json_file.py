#!/usr/bin/python3
"""Task 0"""


from encodings import utf_8
import json


def save_to_json_file(my_obj, filename):
    """function to write file using with"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
