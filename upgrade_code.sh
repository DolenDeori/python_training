#!/bin/bash

PROJECT_DIR="student_management_system"

echo "Upgrading project in '$PROJECT_DIR'..."

# Ensure directory exists
if [ ! -d "$PROJECT_DIR" ]; then
    mkdir "$PROJECT_DIR"
fi

cd "$PROJECT_DIR" || exit

# ==========================================
# 1. MODELS.PY (Updated to hold more data)
# ==========================================
echo "Updating models.py..."
cat << 'EOF' > models.py
class Student:
    def __init__(self, roll_no, name, grade, marks=None, attendance=None, fees_paid=0):
        self.roll_no = roll_no
        self.name = name
        self.grade = grade
        self.marks = marks if marks else {}  # Dictionary: {'Math': 90, 'Science': 85}
        self.attendance = attendance if attendance else []  # List of timestamps
        self.fees_paid = fees_paid

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "grade": self.grade,
            "marks": self.marks,
            "attendance": self.attendance,
            "fees_paid": self.fees_paid
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data.get("roll_no"),
            data.get("name"),
            data.get("grade"),
            data.get("marks"),
            data.get("attendance"),
            data.get("fees_paid", 0)
        )

    def __str__(self):
        return f"[ID: {self.roll_no}] {self.name} | Grade: {self.grade} | Fees: ${self.fees_paid}"
EOF

# ==========================================
# 2. UTILS.PY (New - Reusable Module)
#Req 6: Reusable module
# ==========================================
echo "Creating utils.py..."
cat << 'EOF' > utils.py
def validate_positive_number(value):
    """Reusable function to validate numeric input."""
    try:
        num = float(value)
        if num < 0:
            return False
        return True
    except ValueError:
        return False

def print_header(title):
    """Reusable UI header."""
    print("\n" + "="*30)
    print(f"{title.center(30)}")
    print("="*30)
EOF

# ==========================================
# 3. MARKS.PY (New - Marks Processing)
# Req 3: Marks module
# Req 8: Use 'math' module
# ==========================================
echo "Creating marks.py..."
cat << 'EOF' > marks.py
import math  # Req 8: Predefined module usage

def add_subject_mark(student, subject, score):
    student.marks[subject] = score
    print(f"Added {score} in {subject} for {student.name}.")

def calculate_average(student):
    if not student.marks:
        return 0.0
    total = sum(student.marks.values())
    # Using math.fsum for precise floating point sum (demonstration)
    total_precise = math.fsum(student.marks.values())
    return total_precise / len(student.marks)
EOF

# ==========================================
# 4. ATTENDANCE.PY (New - Attendance)
# Req 7: Separate Attendance module
# Req 8: Use 'datetime' module
# ==========================================
echo "Creating attendance.py..."
cat << 'EOF' > attendance.py
from datetime import datetime  # Req 8: Predefined module usage

def mark_present(student):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    student.attendance.append(now)
    print(f"Marked present for {student.name} at {now}")

def view_attendance(student):
    print(f"Attendance Log for {student.name}:")
    for record in student.attendance:
        print(f" - {record}")
EOF

# ==========================================
# 5. FEES.PY (New - Fee Management)
# Req 7: Separate Fee module
# ==========================================
echo "Creating fees.py..."
cat << 'EOF' > fees.py
def pay_fees(student, amount):
    student.fees_paid += amount
    print(f"${amount} added. Total fees paid: ${student.fees_paid}")
EOF

# ==========================================
# 6. REPORTS.PY (New - Class based)
# Req 4: Report generation using classes
# ==========================================
echo "Creating reports.py..."
cat << 'EOF' > reports.py
class ReportGenerator:
    def __init__(self, students):
        self.students = students

    def generate_full_report(self):
        print("\n--- FULL CLASS REPORT ---")
        for s in self.students:
            avg = 0
            if s.marks:
                avg = sum(s.marks.values()) / len(s.marks)

            print(f"Student: {s.name} (ID: {s.roll_no})")
            print(f"  > Average Marks: {avg:.2f}")
            print(f"  > Days Present: {len(s.attendance)}")
            print(f"  > Fees Paid: ${s.fees_paid}")
            print("-" * 20)
EOF

# ==========================================
# 7. OPERATIONS.PY (Updated Logic)
# Req 2: User defined functions
# Req 8: Use 'random' module
# ==========================================
echo "Updating operations.py..."
cat << 'EOF' > operations.py
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
EOF

# ==========================================
# 8. STORAGE.PY (Unchanged essentially, but rewriting to be safe)
# ==========================================
echo "Updating storage.py..."
cat << 'EOF' > storage.py
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
EOF

# ==========================================
# 9. MAIN.PY (The Integrator)
# Req 5: Demonstrate 'import', 'from..import', 'alias'
# Req 9: Print built-in properties
# ==========================================
echo "Updating main.py..."
cat << 'EOF' > main.py
# Req 5: Demonstrating different import styles
import operations as ops         # Alias
import marks as mk               # Alias
from attendance import mark_present, view_attendance  # From ... Import
import fees                      # Standard import
from reports import ReportGenerator # Class import
import utils

def print_module_introspection(module_obj):
    # Req 9: Print built-in properties (__name__, __file__)
    print(f"\n[DEBUG] Inspecting Module: {module_obj.__name__}")
    print(f"File Location: {module_obj.__file__}")
    # We avoid printing __dict__ because it's too large/messy for console
    print("-" * 30)

def main():
    utils.print_header("MODULAR STUDENT SYSTEM")
    ops.initialize_system()

    while True:
        print("\n1. Add Student (Auto ID)")
        print("2. Add Marks")
        print("3. Mark Attendance")
        print("4. Pay Fees")
        print("5. Generate Reports")
        print("6. Module Introspection (Debug)")
        print("7. Exit")

        choice = input("Choice: ")

        if choice == '1':
            n = input("Name: ")
            g = input("Grade: ")
            ops.add_student(n, g)

        elif choice in ['2', '3', '4']:
            r = input("Enter Roll No: ")
            s = ops.find_student(r)
            if not s:
                print("Student not found.")
                continue

            if choice == '2':
                sub = input("Subject: ")
                score = input("Score: ")
                if utils.validate_positive_number(score):
                    mk.add_subject_mark(s, sub, float(score))
                    avg = mk.calculate_average(s)
                    print(f"New Average: {avg:.2f}")
                    ops.save_changes()
                else:
                    print("Invalid score.")

            elif choice == '3':
                mark_present(s)
                view_attendance(s)
                ops.save_changes()

            elif choice == '4':
                amt = input("Amount: ")
                if utils.validate_positive_number(amt):
                    fees.pay_fees(s, float(amt))
                    ops.save_changes()

        elif choice == '5':
            # Req 4: Using the Report Class
            students = ops.get_all_students()
            reporter = ReportGenerator(students)
            reporter.generate_full_report()

        elif choice == '6':
            # Req 9: Inspecting modules
            print_module_introspection(ops)
            print_module_introspection(mk)
            print_module_introspection(utils)

        elif choice == '7':
            break

if __name__ == "__main__":
    main()
EOF

echo "-------------------------------------------------------"
echo "Upgrade Complete!"
echo "New modules created: marks.py, attendance.py, fees.py, reports.py, utils.py"
echo "Run the system using: python main.py"
echo "-------------------------------------------------------"
