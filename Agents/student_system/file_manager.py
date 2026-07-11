"""File manager for the student system.

Responsible for:
- saving student data to a file
- reading student data from a file

Used by students.py and utilities.py.
"""

FILE_NAME = "students.txt"


def save_students(student_data):
    with open(FILE_NAME, "w") as file:
        for student_id, student_info in student_data.items():
            file.write(f"{student_id},{student_info['name']},{student_info['grade']},{student_info['student_id']}\n")


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = {}
            for line in file:
                line = line.strip()
                if line:
                    student_id, name, grade, stored_student_id = line.split(",")
                    students[student_id] = {
                        "name": name,
                        "grade": float(grade),
                        "student_id": stored_student_id
                    }
            return students
    except FileNotFoundError:
        return {}
