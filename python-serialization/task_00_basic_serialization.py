#!/usr/bin/python3
"""Serializes a Python dictionary, saving it and loading it"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The name of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file into a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
