#!/usr/bin/env python3

"""
Developed by adejonghm
----------

Mar 7, 2023
"""

# Standard libraries imports

# Third-party libraries imports
import streamlit as st



st.set_page_config(layout='wide')
column1, column2 = st.columns(2)

with column1:
    st.image("./images/profile.png", width=300)

with column2:
    st.title('Alejandro de Jongh')
    content = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A cras semper auctor neque vitae tempus.
        Laoreet sit amet cursus sit amet dictum sit. Viverra aliquet eget sit amet tellus cras adipiscing enim. Eget nunc lobortis mattis aliquam faucibus purus.
        Nulla pharetra diam sit amet nisl suscipit adipiscing bibendum est. Arcu bibendum at varius vel pharetra vel turpis nunc eget. Quam quisque id diam vel quam elementum pulvinar.
        Feugiat scelerisque varius morbi enim nunc faucibus. Nulla facilisi nullam vehicula ipsum a arcu cursus vitae. Urna et pharetra pharetra massa massa ultricies mi quis hendrerit.
        Urna id volutpat lacus laoreet non curabitur gravida arcu.
    """
    st.info(content)
