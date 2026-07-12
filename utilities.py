import students


# Calculate the average grade of all students
def calculate_average_grade():
    if not students.student:
        return 0

    grades = [student_data['grade'] for student_data in students.student.values()]
    return round(sum(grades) / len(grades), 2)


# Search for a student by ID and return the result as a dictionary
def search_student(student_id):
    if student_id in students.student:
        student_data = students.student[student_id]
        return {
            'student_id': student_id,
            'name': student_data['name'],
            'grade': student_data['grade']
        }
    return None


average_grade = calculate_average_grade()
