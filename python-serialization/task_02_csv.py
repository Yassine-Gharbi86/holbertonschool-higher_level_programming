#!/usr/bin/python3
"""
Converts CSV data to JSON format and writes it to data.json.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data to JSON format and writes it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read from.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
