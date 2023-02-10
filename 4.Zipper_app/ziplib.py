#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Feb 10, 2023
"""

import zipfile as zf
import pathlib as pl


def zip_files(filepath_arg, dest_folder_arg):
    dest_path = pl.Path(dest_folder_arg, "compressed_files.zip")
    with zf.ZipFile(dest_path, 'w') as zip:
        for filepath in filepath_arg:
            filepath = pl.Path(filepath)
            zip.write(filepath, arcname=filepath.name)


def extract_files(archivepath, dest_dir):
    with zf.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)

