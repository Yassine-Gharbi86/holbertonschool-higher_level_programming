#!/usr/bin/env python3
"""Module that defines mixin classes SwimMixin and FlyMixin,
and a class Dragon that inherits from both."""


class SwimMixin:
    """Mixin class that provides a swim method."""

    def swim(self):
        """Prints a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides a fly method."""

    def fly(self):
        """Prints a message indicating the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon, inheriting from SwimMixin and FlyMixin."""

    def roar(self):
        """Prints a message indicating the dragon roars."""
        print("The dragon roars!")
