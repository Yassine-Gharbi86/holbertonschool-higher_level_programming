#!/usr/bin/python3
"""
This module provides a function to print a name.

Examples:
>>> say_my_name("John", "Smith")
My name is John Smith
>>> say_my_name("Walter", "White")
My name is Walter White
>>> say_my_name("Bob")
My name is Bob
>>> say_my_name(12, "White")
Traceback (most recent call last):
    ...
TypeError: first_name must be a string
>>> say_my_name("John", 12)
Traceback (most recent call last):
    ...
TypeError: last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name.

    Args:
    first_name (str): The first name of the person.
    last_name (str): The last name of the person. Default is an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
