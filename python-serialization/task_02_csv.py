#!/usr/bin/env python3

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert data from a CSV file to JSON format and write to data.json.

    Parameters:
    csv_filename (str): The name of the CSV file to read from.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read the data using DictReader
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON and write to data.json
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    csv_file = "data.csv"
    success = convert_csv_to_json(csv_file)
    if success:
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print("Failed to convert CSV file to JSON.")
