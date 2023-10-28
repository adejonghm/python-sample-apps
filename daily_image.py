#!/usr/bin/env python3

"""
Developed by adejonghm
----------

October 28, 2023
"""

# Standard libraries imports

# Third-party libraries imports
import requests
import streamlit as st


# METADATA
API_KEY = "yzDLPJTGHuWZefA9Glgzzs68CGfPHcLiTzPt1mg0"
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# GET THE REQUEST DATA
req_1 = requests.get(url, timeout=30)
response_data = req_1.json()

# EXTRACTING DATA FROM THE REQUEST
title = response_data['title']
author = response_data['copyright']
image_url = response_data['url']
description = response_data['explanation']

# DOWNLOAD THE IMAGE
image_path = 'image.jpg'
req_2 = requests.get(image_url, timeout=30)

with open(image_path, "wb") as file:
    file.write(req_2.content)

# CREATING THE PAGE
st.title(title)
st.image(image_path)
st.write(description)
