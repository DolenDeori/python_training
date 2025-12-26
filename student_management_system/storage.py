import json
import os

FILE_NAME = "students.json"

def save_to_file(students_list):
    data = [student.to_dict() for student in students_list]
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_file():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except:
        return []
