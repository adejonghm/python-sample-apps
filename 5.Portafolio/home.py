#!/usr/bin/env python3

"""
Developed by adejonghm
----------

March 7, 2023
"""

# Standard libraries imports

# Third-party libraries imports
import pandas as pd
import streamlit as st


st.set_page_config(layout='wide')
data = pd.read_csv("source/data.csv", sep=';')

column1, column2 = st.columns(2)
with column1:
    st.image("images/profile.jpg", width=300)

with column2:
    content = """
        ### Alejandro de Jongh
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A cras semper auctor neque vitae tempus.
        Laoreet sit amet cursus sit amet dictum sit. Viverra aliquet eget sit amet tellus cras adipiscing enim. Eget nunc lobortis mattis aliquam faucibus purus.
        Nulla pharetra diam sit amet nisl suscipit adipiscing bibendum est. Arcu bibendum at varius vel pharetra vel turpis nunc eget.
    """
    st.info(content)

column3, empty_space, column4 = st.columns([2, 0.5, 2])
with column3:
    for index, row in data[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


with column4:
    for index, row in data[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

footer = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""
st.write(footer)
