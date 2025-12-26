import operations

def main():
    print("Initializing System...")
    operations.initialize_system()

    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            r = input("Enter Roll No: ")
            n = input("Enter Name: ")
            g = input("Enter Grade: ")
            operations.add_student(r, n, g)

        elif choice == '2':
            operations.view_all_students()

        elif choice == '3':
            r = input("Enter Roll No to search: ")
            operations.search_student(r)

        elif choice == '4':
            r = input("Enter Roll No to delete: ")
            operations.delete_student(r)

        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
