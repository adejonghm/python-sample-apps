#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Feb 12, 2023
"""

# Standard libraries imports

# Third-party libraries imports
import streamlit as st

# Local libraries imports
import tdlib as fn

toDos = fn.get_toDos()

st.title('To-Do Web App')

st.write("My To-Do list:")
for td in toDos:
    st.checkbox(td)

