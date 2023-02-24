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
    """ Function """
    todo = st.session_state['new_item'] + '\n'
    toDos.append(todo)
    fn.save_toDos(toDos)

# st.set_page_config(layout="wide")
st.title('To-Do Web App')

st.text_input(label="input-todo", key='new_item',
              placeholder="Type here...", label_visibility="hidden",
              on_change=add_new_item)

st.write("<h5><u>My To-Do list:</u></h5>", unsafe_allow_html=True)
for index, td in enumerate(toDos):
    checked = st.checkbox(td, key=td)
    if checked:
        toDos.pop(index)
        fn.save_toDos(toDos)
        del st.session_state[td]
        st.experimental_rerun()
