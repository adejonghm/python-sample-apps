#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Jan 29, 2023
"""


# Standard libraries imports
import os

# Third-party libraries imports
import PySimpleGUI as sg

# Local libraries imports
import tdlib as fn


if not os.path.exists('./database.db'):
    with open('./database.db', 'w') as file:
        pass


label_input = sg.Text('Type a To-Do')
label_list = sg.Text('My To-Do GUI')
input_text = sg.InputText(key='item_to_add', tooltip='Enter the text')
btn_add = sg.Button('Add', key='Add')
btn_edit = sg.Button('Edit', key='Edit')
btn_complete = sg.Button('Done', key='Complete')
listbox = sg.Listbox(values=fn.get_toDos(), key='list_item',
                     enable_events=True, size=[51, 12])
                     
layout = [[label_input], [input_text, btn_add], [label_list], [listbox], [btn_complete, btn_edit]]
window = sg.Window('To-Do List App', layout=layout, font=('Helvetica', 11))

while True:
    event, values = window.read()

    match event:
        case "Add":
            if values['item_to_add'] != '':
                toDos = fn.get_toDos()
                toDos.append(values['item_to_add'].capitalize() + '\n')
                fn.save_toDos(toDos)
            
                window['list_item'].update(values=toDos)
                window['item_to_add'].update(value='')

            else:
                sg.popup('Please, Enter the To-Do you want to add.', title='Warning!', keep_on_top=True)
                
        case "Edit":
            try:
                item_to_edit = values['list_item'][0]
                new_item = values['item_to_add']

                toDos = fn.get_toDos()
                index = toDos.index(item_to_edit)
                toDos[index] = new_item.capitalize() + '\n'
                fn.save_toDos(toDos)

                window['list_item'].update(values=toDos)
                window['item_to_add'].update(value='')

            except IndexError:
                sg.popup('Please, select an item first.', title='Warning!', keep_on_top=True)

        case "Complete":
            try:
                item_to_delete = values['list_item'][0]

                toDos = fn.get_toDos()
                toDos.remove(item_to_delete)
                fn.save_toDos(toDos)

                window['list_item'].update(values=toDos)
                window['item_to_add'].update(value='')

            except IndexError:
                sg.popup('Please, select an item first.', title='Warning!', keep_on_top=True)

        case "list_item":
            item_selected = values['list_item'][0].strip('\n')

            window['item_to_add'].update(value=item_selected)

        case sg.WIN_CLOSED:
            break

window.close()
