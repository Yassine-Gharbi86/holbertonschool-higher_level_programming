#!/usr/bin/python3
"""
Returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The object represented by the JSON string.
    """
    return json.loads(my_str)
