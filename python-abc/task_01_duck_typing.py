#!/usr/bin/env python3
"""Module that defines an abstract class Shape
and its subclasses Circle and Rectangle,
and a function shape_info that uses duck typing
to print the area and perimeter of a shape."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a shape."""

    @abstractmethod
    def area(self):
        """Abstract method for calculating the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for calculating the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initializes the Circle with a radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initializes the Rectangle with width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape.

    Args:
        shape (Shape): An object of type Shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
