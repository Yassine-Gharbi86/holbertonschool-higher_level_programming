#!/usr/bin/env python3
"""Module that defines an abstract class
Animal and its subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method for defining the sound an animal makes."""
        pass


class Dog(Animal):
    """Class representing a dog, inheriting from Animal."""

    def sound(self):
        """Returns the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat, inheriting from Animal."""

    def sound(self):
        """Class representing a cat, inheriting from Animal."""
        return "Meow"
