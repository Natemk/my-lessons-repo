import students


# Calculate the average grade of all students
def calculate_average_grade():
    try:
        grades = [student_data['grade'] for student_data in students.student.values()]
        if not grades:
            return 0.0
        return round(sum(grades) / len(grades), 2)
    except Exception as error:
        print(f"Error calculating average grade: {error}")
        return None


# Search for a student by ID and return the result as a dictionary
def search_student(student_id):
    try:
        if student_id in students.student:
            student_data = students.student[student_id]
            return {
                'student_id': student_id,
                'name': student_data['name'],
                'grade': student_data['grade']
            }
        return None
    except Exception as error:
        print(f"Error searching for student: {error}")
        return None
