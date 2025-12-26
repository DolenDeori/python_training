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
