#!/usr/bin/python3
"""
Module 7-add_item

-Contains a script that adds all arguments to a Python list,
and then save them as a JSON representation in a file
named add_item.json
-If the file doesn’t exist, it should be created
-No exceptions/file permissions management included
"""
import json
import os
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
if os.path.exists(filename):
    file_content = load_from_json(filename)
    save_to_json_file(file_content + argv[1:], filename)
else:
    save_to_json_file(argv[1:], filename)
