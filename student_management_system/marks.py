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
