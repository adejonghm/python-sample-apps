#!/usr/bin/env python3

"""
Developed by adejonghm
----------

November 19, 2023

Flask default port 5000
"""

# Standard libraries imports

# Third-party libraries imports
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/<world>")
def api(world):
    definition = world.upper()
    result = {"World": world,
              "definition": definition}
    return result


if __name__ == '__main__':
    app.run(debug=True, port=4040)
