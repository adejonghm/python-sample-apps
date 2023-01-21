#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Nov 10, 2022
"""

import time


def set_toDos(toDos_arg: list, filepath="todo_list.db"):
    with open(filepath, 'w') as file:
        file.writelines(toDos_arg)


if __name__ == "__main__":
    now = time.strftime("%b %d, %Y %H:%S")
    print("It is", now)

    while True:
        user_action = input("Enter add, show, edit, complete or exit: ")
        user_action = user_action.strip()

        with open("todo_list.db") as file:
            toDos = file.readlines()

        if user_action.startswith('add'):
            item = user_action[4:]
            if item:
                toDos.append(item.capitalize() + '\n')
                set_toDos(toDos)

            else:
                print("*** Please, enter the item you want to add ***\n")

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
                print(
                    "*** Please, enter the item number you want to edit after the command ***\n")
                continue

        elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:])

                index = number - 1

                toDo_to_remove = toDos[index].strip('\n')
                toDos.pop(index)

                set_toDos(toDos)

                print(
                    f"*** Item '{toDo_to_remove}' completed successfully ***\n")

            except IndexError:
                print("*** There is no item with that number ***")
                continue

            except ValueError:
                print(
                    "*** Please, enter the item number you want to compelte after the command ***\n")
                continue

        elif user_action.startswith(('exit', 'quit')):
            break

        else:
            print("*** This command is not valid ***\n")

    print("Bye!")
