#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Nov 10, 2022
"""

toDos = []

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            item = input("Enter the toDo: ")
            toDos.append(item)

        case 'show':
            for index, item in enumerate(toDos):
                print(f"{index + 1}. {item.capitalize()}")

        case 'edit':
            number = int(input("Enter the number or the toDo to edit: "))
            new_item = input("Enter the new ToDo item: ")
            toDos[number - 1] = new_item

        case 'complete':
            number = int(input("Enter the number or the toDo to complete: "))
            toDos.pop(number - 1)

        case 'exit':
            break

        case _:
            print('Command not found')

print('Bye')
