'''
Mini Project

Employee Directory

Requirements:

Store 3 employees
Name
Department
Salary

Display:

Name: John
Department: IT
Salary: 80000

Homework:

1. Create a dictionary for a car:

car = {
    "make": "",
    "model": "",
    "year": 0
}

ask:::::::::::print all keys and values

2. Store students inside a list

students = [
    {
        "name": "John",
        "grade": 85
    },

    {
        "name": "Sarah",
        "grade": 90
    }
]

ask::::::::::::::: Print all student names and grades
'''





def main():
    # Entry point for the student grade program
    print("Student Grade Program")
    print("--------------------")

    # Use a list to keep multiple students, each stored as a dictionary
    students = []

    # Collect student data until the user presses Enter with no name
    while True:
        name = input("Enter student name (or press Enter to finish): ").strip()
        if not name:
            break

        grade_input = input(f"Enter grade for {name}: ").strip()

        # Accept integers or floats with one decimal point
       
        grade = float(grade_input)

        students.append({
            "name": name,
            "grade": grade
        })

    # If the user did not enter any students, use example data instead
    if not students:
        students = [
            {"name": "John", "grade": 85},
            {"name": "Sarah", "grade": 90}
        ]
        print("\nNo student input provided, using sample students.")

    # Display each student's name and grade
    print("\nStudent names and grades:")
    for student in students:
        print(f"{student['name']}: {student['grade']}")


if __name__ == "__main__":
    main()
