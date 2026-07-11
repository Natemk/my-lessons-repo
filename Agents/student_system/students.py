import file_manager

student = file_manager.load_students()


def view_students():
    if not student:
        print("No students found.")
        return

    for student_id, student_data in student.items():
        print(f"ID: {student_id}, Name: {student_data['name']}, Grade: {student_data['grade']}")


def add_student(): 
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    student_id = input("Enter student ID: ")
    
    if not student_id.isdigit():
        raise ValueError("Student ID must be numeric.")
    elif not isinstance(grade, (int, float)):
        raise ValueError("Grade must be a numeric value.")
    elif not name.isalpha():
        raise ValueError("Name must contain only alphabetic characters.")
    
    
    if student_id in student:
        print(f"Student ID {student_id} already exists. Please use a unique ID.")
        return
    else:  
        student[student_id] = {'name': name, 'grade': grade, 'student_id': student_id}
        file_manager.save_students(student)
        print(f"Student {name} added successfully.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    if not student_id.isdigit():
        raise ValueError("Student ID must be numeric.")

    if student_id in student:
        del student[student_id]
        file_manager.save_students(student)
        print(f"Student with ID {student_id} deleted successfully.")
    else:
        print(f"No student found with ID {student_id}.")