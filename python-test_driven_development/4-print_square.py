#!/usr/bin/python3
"""
This module provides a function to print a square.

Examples:
>>> print_square(4)
####
####
####
####
>>> print_square(10)
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########

>>> print_square(0)

>>> print_square(1)
#

>>> try:
...     print_square(-1)
... except Exception as e:
...     print(e)
size must be >= 0
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
    size (int): The size of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
