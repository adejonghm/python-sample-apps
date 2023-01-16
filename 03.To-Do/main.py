#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Nov 10, 2022
"""


while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    with open("database.db") as file:
        toDos = file.readlines()
    
    if user_action.startswith(('add', 'new')):
        item = user_action[4:]
        toDos.append(item.capitalize() + '\n')

        with open("database.db", 'w') as file:
            file.writelines(toDos)

    elif user_action.startswith('show'):
        # new_toDos = [item.strip("\n") for item in toDos]
        for index, item in enumerate(toDos):
            item = item.strip('\n')
            line =f"{index + 1}. {item}" 
            print(line)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            new_item = input("Enter the new ToDo item: ")
            
            toDos[number - 1] = new_item.capitalize() + "\n"

            with open("database.db", 'w') as file:
                file.writelines(toDos)
        except ValueError:
            print('Enter the item number you want to edit after the "edit" command.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            index = number - 1 

            toDo_to_remove = toDos[index].strip('\n')
            toDos.pop(index)

            with open("database.db", 'w') as file:
                file.writelines(toDos)

            print(f"Item '{toDo_to_remove}' completed successfully!")
        
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('This command is not valid.')

print('Bye')
