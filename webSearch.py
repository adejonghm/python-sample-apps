#!/usr/bin/env python3

"""
Developed by adejonghm
----------


"""

# Standard libraries imports
import webbrowser


if __name__ == '__main__':
    user_search = input("Search on Google: ")

    webbrowser.open("https://www.google.com/search?q=" + user_search.replace(" ", "+"))
