#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Jan 29, 2023
"""

# Standard library imports

# Third party imports
import PySimpleGUI as sg
import tdlib as td


label = sg.Text("Type in a To-Do")
input_box = sg.InputText(key='input_box', tooltip='Enter the text')
add_button = sg.Button("Add")

windows = sg.Window('To-Do List App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 11))

while True:
    event, values = windows.read()
    match event:
        case "Add":
            toDos = td.read_toDos()
            toDos.append(values['input_box'].capitalize() + '\n')
            td.save_toDos(toDos)
        
        case sg.WIN_CLOSED:
            break

windows.close()
