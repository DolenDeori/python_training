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
