import storage
from models import Student

# Internal memory list to hold student objects
students = []

def initialize_system():
    """Loads data from file into memory on startup."""
    raw_data = storage.load_from_file()
    for item in raw_data:
        students.append(Student.from_dict(item))

def add_student(roll_no, name, grade):
    # Check if ID already exists
    for s in students:
        if s.roll_no == roll_no:
            print("Error: Roll Number already exists.")
            return

    new_student = Student(roll_no, name, grade)
    students.append(new_student)
    storage.save_to_file(students)
    print(f"Student {name} added!")

def view_all_students():
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for s in students:
            print(s)
        print("--------------------")

def search_student(roll_no):
    for s in students:
        if s.roll_no == roll_no:
            print(f"\nFound: {s}")
            return
    print("Student not found.")

def delete_student(roll_no):
    global students
    # Filter out the student with the matching roll_no
    initial_count = len(students)
    students = [s for s in students if s.roll_no != roll_no]

    if len(students) < initial_count:
        storage.save_to_file(students)
        print("Student deleted.")
    else:
        print("Student not found.")
