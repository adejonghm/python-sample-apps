#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Jan 29, 2023
"""

# Standard library imports

# Third party imports
import PySimpleGUI as sg
import tdlib as fn


label_input = sg.Text('Type a To-Do')
label_list = sg.Text('My To-Do list')
input_text = sg.InputText(key='item_to_add', tooltip='Enter the text')
btn_add = sg.Button('Add', key='Add')
listbox = sg.Listbox(values=fn.get_toDos(), key='list_item',
                     enable_events=True, size=[51, 12])
                     
layout = [[label_input], [input_text, btn_add], [label_list], [listbox],]
window = sg.Window('To-Do List App', layout=layout, font=('Helvetica', 11))

while True:
    event, values = window.read()

    match event:
        case "Add":
            toDos = fn.get_toDos()
            toDos.append(values['item_to_add'].capitalize() + '\n')
            fn.save_toDos(toDos)
            
            window['list_item'].update(values=toDos)
            window['item_to_add'].update(value='')

        case sg.WIN_CLOSED:
            break

window.close()
