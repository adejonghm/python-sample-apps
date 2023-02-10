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
input_files = sg.Input()
input_destination = sg.Input()

# Buttons
btn_files = sg.FilesBrowse("Choose", key='files')
btn_destination = sg.FolderBrowse("Choose", key='folder')
btn_compress = sg.Button("Compress", key='compress')


layout = [[label_files], [input_files, btn_files],
          [label_destination], [input_destination, btn_destination],
          [btn_compress, label_success]]
window = sg.Window('File Zipper', layout=layout, font=("Helvetica", 11))

while True:
    event, elements = window.read()

    match event:
        case "compress":
            if elements['files'] == "" or elements['folder'] == "":
                sg.popup('Please, select the files or destination!', title='Warning!', keep_on_top=True)

            else:
                filepaths = elements['files'].split(';')
                folderpath = elements['folder']
                zl.zip_files(filepaths, folderpath)
            
                window['success'].update(value="Compression Completed!")
 
        case sg.WIN_CLOSED:
            break

window.close()

