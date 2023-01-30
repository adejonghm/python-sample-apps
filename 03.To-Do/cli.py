#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Nov 10, 2022
"""

import time


FILE = "todo_list.db"


def set_toDos(toDos_arg: list, filepath=FILE):
    with open(filepath, 'w') as file:
        file.writelines(toDos_arg)


if __name__ == "__main__":
    now = time.strftime("%b %d, %Y %H:%S")
    print("It is", now)

    while True:
        print("Use one of the following commands [add, show, edit, complete or exit]")
        user_action = input("Enter the command: ")
        user_action = user_action.strip()

        with open(FILE) as file:
            toDos = file.readlines()

        if user_action.startswith('add'):
            item = user_action[4:]
            if item:
                toDos.append(item.capitalize() + '\n')
                set_toDos(toDos)

            else:
                print("*** Type the ToDo item you want to ADD after the command. ***\n")

        elif user_action.startswith('show'):
            # new_toDos = [item.strip("\n") for item in toDos]
            for index, item in enumerate(toDos):
                item = item.strip('\n')
                line = f"{index + 1}. {item}"
                print(line)

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])
                new_item = input("Enter the new ToDo item: ")

                toDos[number - 1] = new_item.capitalize() + "\n"

                set_toDos(toDos)

            except ValueError:
                print("*** Type the item number you want to EDIT after the command. ***\n")
                continue

        elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:])

                index = number - 1

                toDo_to_remove = toDos[index].strip('\n')
                toDos.pop(index)

                set_toDos(toDos)

                print(
                    f"*** Item '{toDo_to_remove}' completed successfully. ***\n")

            except IndexError:
                print("*** There is no ITEM with that number. ***\n")
                continue

            except ValueError:
                print("*** Type the item number you want to COMPLETE after the command. ***\n")
                continue

        elif user_action.startswith(('exit', 'quit')):
            break

        else:
            print("*** Please enter a valid command. ***\n")

    print("Bye!")
