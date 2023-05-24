#!/usr/bin/env python3

"""
Developed by adejonghm
----------

May 19, 2023
"""
# Standard libraries imports
from pathlib import Path
import glob

# Third-party libraries imports
from fpdf import FPDF
import pandas as pd


if __name__ == '__main__':
    filepaths = glob.glob("./invoices/*.xlsx")
    column_width = (35, 60, 40, 30, 25)
    height = 8

    # Loading Excel files
    for filepath in filepaths:
        filename = Path(filepath).stem
        invoice_nr, date = filename.split('-')

        pdf = FPDF(orientation='P', format='A4', unit='mm')
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.add_page()

        # Set Page header
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.set_text_color(120, 120, 120)
        pdf.cell(w=0, h=8, txt="AJTech Company", align='R', ln=1)
        pdf.line(5, 17, 205, 17)

        # Add Document header
        pdf.set_font(family='Times', size=16, style='B')
        pdf.set_text_color(20, 20, 20)
        pdf.cell(w=0, h=3, txt="", ln=1)
        pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Date {date}", ln=1)
        pdf.cell(w=0, h=3, txt="", ln=1)

        # Read Excel file
        df = pd.read_excel(filepath, sheet_name="Sheet 1")
        columns = list(df.columns)
        
        # Add Table header
        columns_name = [item.replace("_", " ").title() for item in columns]
        length = len(columns)
        pdf.set_font(family='Times', size=12, style='B')
        for index in range(length):
            if index == length - 1:
                pdf.cell(w=column_width[index], h=height, txt=columns_name[index], border=1, ln=1)
            else:
                pdf.cell(w=column_width[index], h=height, txt=columns_name[index], border=1)

        # Add rows
        pdf.set_font(family='Times', size=10)
        for _, row in df.iterrows():
            for index in range(length):
                row_name = columns[index]
                if index == length - 1:
                    pdf.cell(w=column_width[index], h=height, txt=str(row[row_name]), border=1, ln=1)
                else:
                    pdf.cell(w=column_width[index], h=height, txt=str(row[row_name]), border=1)

        # Add total price.
        total_price = df['total_price'].sum()
        pdf.set_font(family='Times', size=13, style='B')
        pdf.cell(w=0, h=5, txt="", ln=1)
        pdf.cell(w=0, h=8, txt=f'The total price is: ${total_price}', align='R', ln=1)

        pdf.output(f"pdfs/{filename}.pdf")
