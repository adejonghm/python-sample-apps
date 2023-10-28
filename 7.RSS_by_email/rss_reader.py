#!/usr/bin/env python3

"""
Developed by adejonghm
----------

October 25, 2023
"""

# Standard libraries imports

# Third-party libraries imports
import requests

# Local libraries imports
from sendMail import send_email


API_KEY = 'ccb1bf8ed7e34910b1809e41021786a3'
TOPIC = 'tesla'
ORDER = 'publishedAt'
DATE = '2023-09-28'
LANG = 'en'

url = "https://newsapi.org/v2/everything?" \
    f"q={TOPIC}&" \
    f"from=&{DATE}" \
    f"sortBy={ORDER}&" \
    f"apiKey={API_KEY}&" \
    f"language={LANG}"

request = requests.get(url, timeout=30)
content = request.json()

body = ""
for article in content["articles"]:
    title = article['title']
    description = article['description']
    url = article['url']

    if (title is not None) and (description is not None) and (url is not None):
        body = body \
            + f"Subject: Today's News about {TOPIC.title()}" + "\n" \
            + title + "\n" \
            + description + "\n" \
            + "Link: " + url + 2*"\n"


send_email(body.encode("utf-8"))
