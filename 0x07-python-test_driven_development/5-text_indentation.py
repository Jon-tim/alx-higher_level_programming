#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
No space at the beginning or end of each printed line
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    add_newline = False

    for char in text:
        if char in ['.', '?', ':']:
            new_text += char + '\n\n'
            add_newline = True
        else:
            if char == ' ' and add_newline:
                continue
            new_text += char
            add_newline = False

    print(new_text, end='')
