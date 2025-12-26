import json
import os

FILE_NAME = "students.json"

def save_to_file(students_list):
    """Saves a list of Student objects to a JSON file."""
    # Convert list of objects to list of dictionaries
    data = [student.to_dict() for student in students_list]

    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully.")

def load_from_file():
    """Loads data from JSON file and returns a list of dictionaries."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
