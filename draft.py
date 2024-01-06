#!/usr/bin/env python3

"""
Developed by adejonghm
----------

"""

# import streamlit as st

# -------- Trabajando con dos columnas --------
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")


# -------- Progress Bar --------
# import streamlit as st
# import time

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)
# st.write('...and now we\'re done!')


# -------- Capturando imagen con la camara --------
# from PIL import Image

# st.subheader("Color to Grayscale Converter")

# ## Using uploader file
# imported_image = st.file_uploader('Upload an image')

# if imported_image:
#     img = Image.open(imported_image)
#     gray_imported_image = img.convert('L')
#     st.image(gray_imported_image)

# ## Using the webcam
# with st.expander('Start camera'):
#     camera_image = st.camera_input('Camera')

# if camera_image:
#     img = Image.open(camera_image)
#     gray_camera_img = img.convert('L')
#     st.image(gray_camera_img)
