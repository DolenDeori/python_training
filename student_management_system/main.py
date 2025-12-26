import operations as ops
import marks as mk
from attendance import mark_present, view_attendance
import fees
from reports import ReportGenerator
import utils

def print_module_introspection(module_obj):
    print(f"\n[DEBUG] Inspecting Module: {module_obj.__name__}")
    print(f"File Location: {module_obj.__file__}")
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
