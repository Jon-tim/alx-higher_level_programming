#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file:
"""
import sys
from pathlib import Path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def load_add_save():
    """
    load and save
    """
    file = "add_item.json"
    arguments = sys.argv[1:]

    if Path(file).is_file():
        exsting_list = load_from_json_file(file)
        exsting_list.extend(arguments)
        save_to_json_file(exsting_list, file)
    else:
        save_to_json_file(arguments, file)


load_add_save()
