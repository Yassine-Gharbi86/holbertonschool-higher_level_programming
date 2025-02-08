#!/usr/bin/python3
"""Module that defines a class BaseGeometry
with a method area that raises an Exception."""


class BaseGeometry:
    """A class named BaseGeometry."""

    def area(self):
        """Raises an Exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")
