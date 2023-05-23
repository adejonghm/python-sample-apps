#!/usr/bin/env python3

"""
Developed by adejonghm
----------

May 23, 2023
"""

# Standard libraries imports
from pathlib import Path
import glob

# Third-party libraries imports
from fpdf import FPDF
import pandas as pd

if __name__ == '__main__':
    filepaths = glob.glob('./source/*.txt')
    # Create PDFs
    pdf = FPDF(orientation='P', format='A4', unit='mm')

    for filepath in filepaths:
        # Add a page for each txt file
        pdf.add_page()

        # Get the filename and convert it to Title Case
        filename = Path(filepath).stem
        name = filename.title()

        # Add the name
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=40, h=10, txt=f"{name}:", ln=1)

        with open(filepath) as file:
            content = file.read()

        pdf.set_font(family='Times', size=12)
        pdf.multi_cell(w=0, h=6, txt=content)

    pdf.output("report.pdf")
