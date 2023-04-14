#!/usr/bin/env python3

"""
Developed by adejonghm
----------

April 14, 2023
"""

# Standard libraries imports

# Third-party libraries imports
from fpdf import FPDF
import pandas as pd

dataFrame = pd.read_csv("./source/topics.csv")
pdf = FPDF(orientation='P', format='A4', unit="mm")

for index, row in dataFrame.iterrows():
    pdf.add_page()
    
    pdf.set_font(family='Arial', style='B', size=14)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=0, align="L")
    pdf.line(10, 19, 200, 19)

pdf.output("template.pdf")