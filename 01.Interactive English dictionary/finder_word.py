#!/usr/bin/env python3

"""
Developed by adejonghm
----------


"""

# Standard library imports
import json
from difflib import get_close_matches


with open('dictionary.json') as file:
    dictionary = json.load(file)


def search(word):
    word = word.lower()

    if word in dictionary:
        return dictionary[word]
    elif word.title() in dictionary:
        return dictionary[word.title()]
    elif word.upper():
        return dictionary[word.upper()]
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        yes_no = input('Did you mean "{}"? Please, enter Yes/No: '.format(
            get_close_matches(word, dictionary.keys(), )[0]))
        if yes_no.lower() == 'yes':
            return dictionary[get_close_matches(word, dictionary.keys(), )[0]]
        elif yes_no.lower() == 'no':
            return "The word doesn't exist."
        else:
            return "It is not possible to execute this option."
    else:
        return "The word doesn't exist."


word = input("Enter the world: ")

found = search(word)

if type(found) == list:
    for definition in found:
        print("Definition: {}".format(definition))
elif found.startswith(("The", "It")):
    print(found)
else:
    print("Definition: {}".format(found))
