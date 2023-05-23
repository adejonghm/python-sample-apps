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


if __name__ == '__main__':

    dataFrame = pd.read_csv("./source/topics.csv")
    pdf = FPDF(orientation='P', format='A4', unit="mm")
    pdf.set_auto_page_break(auto=False, margin=0)

    for index, row in dataFrame.iterrows():
        pdf.add_page()

        # Set Header
        pdf.set_font(family='Arial', style='B', size=14)
        pdf.set_text_color(10, 10, 10)
        pdf.cell(w=0, h=12, txt=row["Topic"], ln=0, align="L")
        pdf.line(10, 19, 200, 19)

        # Set Footer
        pdf.ln(270)
        pdf.set_font(family='Arial', style='B', size=9)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], ln=0, align="R")

    pdf.output("template.pdf")
