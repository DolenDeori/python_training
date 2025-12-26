import storage
from models import Student
import random  # Req 8: Predefined module usage

students = []

def initialize_system():
    raw_data = storage.load_from_file()
    global students
    students = [Student.from_dict(item) for item in raw_data]

def save_changes():
    storage.save_to_file(students)

def generate_id():
    """Generates a random 4-digit ID."""
    return str(random.randint(1000, 9999))

def add_student(name, grade):
    roll_no = generate_id()
    new_student = Student(roll_no, name, grade)
    students.append(new_student)
    save_changes()
    print(f"Student added with Auto-ID: {roll_no}")

def find_student(roll_no):
    for s in students:
        if s.roll_no == roll_no:
            return s
    return None

def get_all_students():
    return students
