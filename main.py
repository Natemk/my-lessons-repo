import students
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

        choice = input("Select an option: ").strip()

        try:
            if choice == '1':
                students.add_student()
            elif choice == '2':
                result = utilities.calculate_average_grade()
                if result is None:
                    print("No average grade available.")
                else:
                    print(f"Average Grade: {result}")
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
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
    
#shop - location, product, price
#construction -machinery, contract and site
#math -divide, multiply, add, subtract