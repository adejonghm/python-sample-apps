#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Jan 30, 2023
"""

import PySimpleGUI as sg
import ziplib as zl


sg.theme('DarkBlack1')

# Labels
label_files = sg.Text("Select an archive:")
label_destination = sg.Text("Select the destination folder:")
label_success = sg.Text(key='success', text_color='green')

# Input Text
input_files = sg.Input(key='zipfile')
input_destination = sg.Input(key='destination')

# Buttons
btn_files = sg.FileBrowse("Choose", key='file')
btn_destination = sg.FolderBrowse("Choose", key='folder')
btn_compress = sg.Button("Extract", key='extract')


layout = [[label_files], [input_files, btn_files],
          [label_destination], [input_destination, btn_destination],
          [btn_compress, label_success]]
window = sg.Window('File Zipper', layout=layout, font=("Helvetica", 11))

while True:
    event, elements = window.read()

    match event:
        case "extract":
            try:
                if elements['file'].split('.')[-1] != 'zip':
                    sg.popup('Please, select a ZIP file', title='Warning!', keep_on_top=True)

                else:
                    filepath = elements['file']
                    folderpath = elements['folder']
                    zl.extract_files(filepath, folderpath)

                    sg.popup('Extraction Completed!', title='Success!', keep_on_top=True)
                    window['zipfile'].update(value="")
                    window['destination'].update(value="")
            
            except FileNotFoundError:
                sg.popup('Please, select a Zip file.', title='Warning!', keep_on_top=True)
    
        case sg.WIN_CLOSED:
            break

window.close()

