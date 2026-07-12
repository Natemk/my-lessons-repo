"""File manager for the student system.

Responsible for:
- saving student data to a file
- reading student data from a file

Used by students.py and utilities.py.
"""

# Name of the text file where student data will be stored
FILE_NAME = "students.txt"


# Save all students to a text file
def save_students(student_data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for student_id, student_info in student_data.items():
            file.write(f"{student_id},{student_info['name']},{student_info['grade']}\n")


# Load students from the text file back into memory
def load_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            students = {}
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = [part.strip() for part in line.split(",")]
                if len(parts) != 3:
                    continue

                student_id, name, grade_text = parts

                try:
                    grade = float(grade_text)
                except ValueError:
                    continue

                students[student_id] = {
                    "name": name,
                    "grade": grade,
                    "student_id": student_id
                }
            return students
    except FileNotFoundError:
        return {}
