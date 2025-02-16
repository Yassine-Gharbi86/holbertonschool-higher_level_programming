#!/usr/bin/python3
"""Class representing a custom object."""
import pickle


class CustomObject:
    """Class representing a custom object."""

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error occurred while serializing: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from a file.

        Args:
            filename (str): The name of the file to load the serialized object.

        Returns:
            CustomObject: The deserialized CustomObject instance,
            or None if an error occurs.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error occurred while deserializing: {e}")
            return None
