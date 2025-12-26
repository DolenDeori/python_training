from datetime import datetime  # Req 8: Predefined module usage

def mark_present(student):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    student.attendance.append(now)
    print(f"Marked present for {student.name} at {now}")

def view_attendance(student):
    print(f"Attendance Log for {student.name}:")
    for record in student.attendance:
        print(f" - {record}")
