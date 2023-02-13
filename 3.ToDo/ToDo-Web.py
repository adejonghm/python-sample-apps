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


def add_new_item():
    todo = st.session_state['new_item'] + '\n'
    toDos.append(todo)

    fn.save_toDos(toDos)


st.title('To-Do Web App')

st.write("My To-Do list:")
for td in toDos:
    st.checkbox(td)

st.text_input("Enter the To-Do:", on_change=add_new_item,
              placeholder="Type here...", key='new_item')
