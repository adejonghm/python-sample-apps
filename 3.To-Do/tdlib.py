#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Jan 31, 2023
"""

FILE = "todo_list.db"


def read_toDos(filepath=FILE):
    with open(FILE) as file:
        todos_list = file.readlines()
    
    return todos_list


def save_toDos(toDos_arg: list, filepath=FILE):
    with open(filepath, 'w') as file:
        file.writelines(toDos_arg)
