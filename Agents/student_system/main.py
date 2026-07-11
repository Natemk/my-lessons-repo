import students
import file_manager
import utilities


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            students.add_student()
        elif choice == '2':
            students.view_students()
        elif choice == '3':
            students.search_student()
        elif choice == '4':
            students.delete_student()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()