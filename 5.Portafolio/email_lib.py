#!/usr/bin/env python3

"""
Developed by adejonghm
----------

March 14, 2023
"""

# Standard libraries imports
import os

# Third-party libraries imports
import ssl
import smtplib


def send_email(message):
    """ Description
    """
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("GMAIL_USERNAME")
    password = os.getenv("GMAIL_PASSWORD")

    receiver = "mailserver4everything@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
