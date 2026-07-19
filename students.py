import file_manager

# Load students from file when the program starts
student = file_manager.load_students()


# Show all students in the dictionary
def view_students():
    if not student:
        print("No students found.")
        return

    for student_id, student_data in student.items():
        print(f"ID: {student_id}, Name: {student_data['name']}, Grade: {student_data['grade']}")


# Add a new student to the dictionary and save it to the file
def add_student():
    try:
        name = input("Enter student name: ").strip()
        grade_text = input("Enter student grade: ").strip()
        student_id = input("Enter student ID: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")
        if not all(part.isalpha() for part in name.split() if part):
            raise ValueError("Name must contain only alphabetic characters and spaces.")

        try:
            grade = float(grade_text)
        except ValueError:
            raise ValueError("Grade must be a numeric value.") from None

        if not student_id.isdigit():
            raise ValueError("Student ID must be numeric.")

        if student_id in student:
            raise ValueError(f"Student ID {student_id} already exists. Please use a unique ID.")

        student[student_id] = {'name': name, 'grade': grade, 'student_id': student_id}
        file_manager.save_students(student)
        print(f"Student {name} added successfully.")
    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


# Search for a student using their ID
def search_student():
    try:
        student_id = input("Enter student ID to search: ").strip()
        if student_id in student:
            student_data = student[student_id]
            print(f"ID: {student_id}, Name: {student_data['name']}, Grade: {student_data['grade']}")
        else:
            print(f"No student found with ID {student_id}.")
    except Exception as error:
        print(f"Error: {error}")


# Delete a student by their ID
def delete_student():
    try:
        student_id = input("Enter student ID to delete: ").strip()
        if not student_id.isdigit():
            raise ValueError("Student ID must be numeric.")

        if student_id in student:
            del student[student_id]
            file_manager.save_students(student)
            print(f"Student with ID {student_id} deleted successfully.")
        else:
            print(f"No student found with ID {student_id}.")
    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")