#!/usr/bin/python3
"""module"""
import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = 'add_item.json'

try:
    with open(filename, 'r') as f:
        pass
except FileNotFoundError as err:
    with open(filename, 'w') as f:
        pass

try:
    previous = load_from_json_file(filename)
    save_to_json_file(previous + sys.argv[1:], filename)
except json.decoder.JSONDecodeError as err:
    save_to_json_file(sys.argv[1:], filename)
