#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Jan 31, 2023
"""

FILE_DB = "./database.db"


def get_toDos(filepath=FILE_DB):
    with open(FILE_DB) as file:
        todos_list = file.readlines()
    
    return todos_list


def save_toDos(toDos_arg: list, filepath=FILE_DB):
    with open(FILE_DB, 'w') as file:
        file.writelines(toDos_arg)
