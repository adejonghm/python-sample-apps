#!/usr/bin/env python3

"""
Developed by adejonghm
----------

November 21, 2023
"""


import pandas as pd

df = pd.read_csv("./data_small/TG_STAID000003.txt", skiprows=20, parse_dates=["    DATE"])

print(df)
