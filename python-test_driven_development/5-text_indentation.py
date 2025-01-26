#!/usr/bin/python3
"""
This module provides a function to indent text.

Examples:
>>> text_indentation("Hello world: this is a test.")
Hello world:
<BLANKLINE>
this is a test.
<BLANKLINE>

>>> text_indentation(123)
Traceback (most recent call last):
    ...
TypeError: text must be a string

>>> text_indentation("")
Traceback (most recent call last):
    ...
TypeError: text must be a string
"""


def text_indentation(text):
    """
    Indents text.

    Args:
    text (str): The text to indent.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str) or text == "":
        raise TypeError("text must be a string")
    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in '.?:':
            print("\n")
            while i + 1 < length and text[i + 1] == " ":
                i += 1
        i += 1
