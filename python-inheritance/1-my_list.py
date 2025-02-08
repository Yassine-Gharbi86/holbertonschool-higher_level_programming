#!/usr/bin/python3
"""Module that defines the class MyList, inheriting from list."""


class MyList(list):
    """Represents a list with an additional method to print sorted list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
