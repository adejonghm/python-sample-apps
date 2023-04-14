#!/usr/bin/env python3

"""
Developed by adejonghm
----------

March 14, 2023
"""

# Third-party libraries imports
import pandas as pd
import streamlit as st

# Local libraries imports
import sendMail as sm


data = pd.read_csv("source/topics.csv")
st.header("Contact Me")

with st.form(key="contact_form"):
    user_name = st.text_input("Your name")
    user_email = st.text_input("Your email address")
    topic = st.selectbox('What topic do you want to discuss?', data['topic'])
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Someone contacted you with a {topic}.

{raw_message}

---
From: {user_name}
Email: {user_email}
"""
    button = st.form_submit_button("Submit")

    if button:
        sm.send_email(message)
        st.info("Your message sent successfully!")
