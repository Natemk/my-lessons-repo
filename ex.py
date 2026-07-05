# Student grade tracking and file-based student database

# Create an empty list to store student names
students = []

# Ask the user to enter 5 student names
for i in range(5):
    name = input(f"Enter name of student {i + 1}: ").capitalize()
    students.append(name)

print("\nStudents entered are:")
for student in students:
    print(student)

# Create an empty list to store the corresponding grades
grades = []
for student in students:
    grade = float(input(f"Enter grade for {student}: "))
    grades.append(grade)

    # Print the letter grade for each student as the grade is entered
    if grade >= 90:
        print(f"{student} received an A.\n")
    elif grade >= 80:
        print(f"{student} received a B.\n")
    elif grade >= 70:
        print(f"{student} received a C.\n")
    elif grade >= 60:
        print(f"{student} received a D.\n")
    else:
        print(f"{student} received an F.\n")

# Pair each student with their grade for sorting
student_grades = list(zip(students, grades))

# Sort the list of (student, grade) pairs by grade in descending order
student_grades.sort(key=lambda pair: pair[1], reverse=True)

print("Students and grades in descending order:")
for student, grade in student_grades:
    print(f"{student}: {grade}")

# --- File-based student database menu ---
with open("student.txt", "a") as file:
    pass

while True:
    print("\n=== STUDENT DATABASE MENU ===")
    print("1. Write (Add new student)")
    print("2. Update (Change a student's grade/details)")
    print("3. Remove (Delete a student)")
    print("4. Display (Show all stored data)")
    print("(Press ENTER without typing anything to Exit)")

    choice = input("\nSelect an option: ")

    if choice == "":
        print("Exiting program. Goodbye!")
        break

    if choice == "1" or choice.lower() == "write":
        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")

        with open("student.txt", "a") as file:
            file.write(name + ":" + grade + "\n")
        print("Student Registered Successfully!")

    elif choice == "2" or choice.lower() == "update":
        search_name = input("Enter the name of the student to update: ")

        students_from_file = {}
        with open("student.txt", "r") as file:
            for line in file:
                if ":" in line:
                    key, value = line.split(":", 1)
                    students_from_file[key.strip()] = value.strip()

        if search_name in students_from_file:
            new_grade = input("Enter new grade for " + search_name + ": ")
            students_from_file[search_name] = new_grade

            with open("student.txt", "w") as file:
                for key, value in students_from_file.items():
                    file.write(key + ":" + value + "\n")
            print("Student grade updated successfully!")
        else:
            print("Student not found.")

    elif choice == "3" or choice.lower() == "remove":
        search_name = input("Enter the name of the student to remove: ")

        students_from_file = {}
        with open("student.txt", "r") as file:
            for line in file:
                if ":" in line:
                    key, value = line.split(":", 1)
                    students_from_file[key.strip()] = value.strip()

        if search_name in students_from_file:
            del students_from_file[search_name]

            with open("student.txt", "w") as file:
                for key, value in students_from_file.items():
                    file.write(key + ":" + value + "\n")
            print(search_name + " has been removed.")
        else:
            print("Student not found.")

    elif choice == "4" or choice.lower() == "display":
        print("\n--- Current Registered Students ---")
        with open("student.txt", "r") as file:
            content = file.read()

        if content.strip() == "":
            print("[Database is empty]")
        else:
            print(content)

    else:
        print("Invalid choice! Please select an option from the menu.")
