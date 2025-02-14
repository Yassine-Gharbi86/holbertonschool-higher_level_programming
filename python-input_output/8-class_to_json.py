#!/usr/bin/python3
"""
Returns the dictionary description
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj: The instance of the class to be serialized.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
