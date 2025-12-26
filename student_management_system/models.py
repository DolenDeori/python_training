class Student:
    def __init__(self, roll_no, name, grade):
        self.roll_no = roll_no
        self.name = name
        self.grade = grade

    def to_dict(self):
        """Convert student object to a dictionary for saving."""
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        """Create a Student object from a dictionary."""
        return Student(data["roll_no"], data["name"], data["grade"])

    def __str__(self):
        return f"[ID: {self.roll_no}] {self.name} - Grade: {self.grade}"
