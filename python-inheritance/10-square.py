#!/usr/bin/python3
"""Module that defines a class Square inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named Square inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes the Square with size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the square."""
        return f"[Rectangle] {self.__size}/{self.__size}"
