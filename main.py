import students
import file_manager
import utilities


# Main menu for the student management system
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Average Grade")
        print("3. View Students")
        print("4. Search Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            students.add_student()
        elif choice == '2':
            utilities.calculate_average_grade()
        elif choice == '3':
            students.view_students()
        elif choice == '4':
            students.search_student()
        elif choice == '5':
            students.delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()