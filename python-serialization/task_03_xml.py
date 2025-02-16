#!/usr/bin/python3
"""
Serializes a Python dictionary to XML and saves it to a file,
Deserializes XML data from a file and returns a Python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to a file.

    Args:
        dictionary (dict): The Python dictionary to be serialized.
        filename (str): The name of the output XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"Error occurred while serializing to XML: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file and returns a Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except Exception as e:
        print(f"Error occurred while deserializing from XML: {e}")
        return None
