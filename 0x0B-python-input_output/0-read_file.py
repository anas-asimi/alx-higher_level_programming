#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """function"""
    with open(filename) as f:
        for line in f:
            print(line, end='')
